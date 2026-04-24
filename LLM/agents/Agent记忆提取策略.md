## 面试问答
- 提问："Agent 的记忆提取触发策略"？
	- agent 系统工程权衡的理解
- 答
	1. **本质**： "记忆提取有成本，每次触发要额外调一次 LLM，所以触发策略的核心是在**成本控制和记忆覆盖率之间取平衡**。"
	2. **主流策略**；
					1.  "一类是规则驱动：Claude Code 用消息数量阈值（≥4条），Generative Agents 用重要性积分阈值，触发时机确定可预测。
					2.  另一类是 LLM 自主驱动：MemGPT 让 LLM 通过函数调用自己决定何时读写记忆，灵活但非确定性。"
	3. **提取结果处理**
		1. Mem0 用 ADD/UPDATE/DELETE/NOOP 四种操作，NOOP 表示没有有价值的新信息，避免无效写入。
	4. **项目实践：**
		 1. "在我们的 Agent 项目里，用的是类似 Claude Code 的后台异步策略，每 N 条新消息触发一次，用单独的任务异步执行不阻塞主对话。触发后 LLM 扫描新增内容，有新信息才写入，没有就跳过。实测下来 API 调用次数比每轮触发降低了约 60%，记忆覆盖率没有明显下降。"

---
## 背景知识
"`记忆提取`"是指：
- 从对话历史中识别出值得长期保存的信息，写入持久化存储。这个过程本质上要调用一次 LLM，让它判断"这段对话里有什么值得记"。
- 通常提取的内容：
	- 用户偏好、稳定事实、任务状态、阶段性结论/摘要、应用级知识
- —— 这是额外的 API 调用，有成本，有延迟。
- 关键问题，如何设计触发策略，在成本控制和记忆覆盖率之间平衡

### Claude Code 的策略 ：消息数量阈值 + Coalescing 防并发
- **数量阈值**
	- 触发条件：MIN_NEW_MESSAGES = 4
		- 为什么是4，经验阈值
```python
increment = len(messages) - self._watermark  # 与上次提取时的消息数之差  
if increment >= MIN_NEW_MESSAGES:             # MIN_NEW_MESSAGES = 4  
	 await extract_memories(messages, memory_dir, model)  
	 self._watermark = len(messages)
```
当新增消息数达到4时，才触发 `extract_memories`

- **Coalescing,合并：防止并发写乱**
	- 并发问题，用户快速连续输入多轮，前一次提取还没跑完，新一轮又来了
	- 解决，claude code通过合并来处理。
		- 确保延迟不会叠加
		- 中间信息不会丢失
		- 只要有新消息，最终一定会被看到
```
_running: bool = False   # 是否有提取正在运行  
_dirty: bool = False     # 运行中是否有新请求进来  
_watermark: int = 0      # 上次提取时的消息水位
```
逻辑流程是：
1. 来了新请求，如果 `_running` 为 True，直接设 `_dirty = True` 返回，不启动新提取
2. 如果 `_running` 为 False，加锁，开始提取，设 `_running = True`
3. 提取完成后检查 `_dirty`：如果为 False，说明提取过程中没有新消息，直接退出
4. 如果 `_dirty` 为 True，清除标记，**重新跑一轮提取**，扫描提取过程中新增的消息
5. 循环直到 `_dirty` 为 False

工作流程，典型“竞争者”合并模式
![](others/Pasted%20image%2020260423164028.png)

---

### Generative Agents：基于重要性积分触发反思
> 2023 年的一篇经典论文，“Generative Agents: Interactive Simulacra of Human Behavior”

**Memory Stream + 重要性评分**
- 所有agent经历的事件写入Memory Stream并打分
- 当打分超出阈值
- 将最近100条触发，反思，生成更抽象洞察
- 与claude（时钟驱动）区别，事件驱动
- 优点，缺点。
```
触发逻辑：
 importance_sum += new_memory.importance_score
 if importance_sum >= REFLECTION_THRESHOLD:  # 150
     run_reflection(recent_memories[-100:])
     importance_sum = 0  # 重置
```

**检索策略，三维评分**
```
score = α × recency_score + β × importance_score + γ × relevance_score
```
- recency_score：时间衰减，越近的记忆分越高，公式是 decay_rate ^ hours_passed，论文默认 decay_rate = 0.995
- importance_score：写入时打的重要性分
- relevance_score：Query 与记忆的语义相似度
目标，
- 既考虑"跟当前问题有多相关"，也考虑"这件事多重要"，还考虑"这件事是不是很久以前的了"。

### MemGPT(2023)：让 LLM 自己决定什么时候写记忆
> 论文 **“MemGPT: Towards LLMs as Operating Systems”**。它的核心目标是解决 LLM **上下文窗口有限** 的问题：不是一味把 context 变大，而是借鉴操作系统的**虚拟内存/分层内存管理**思路，让模型学会在“快但小的上下文”和“慢但大的外部存储”之间搬运信息，从而给用户一种“近似无限上下文”的体验。

类比虚拟内存

### Mem0(2025)：用 CRUD 操作规范化提取结果
> 论文，Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

**四种操作类型**
- 规范提取结果分类，只有四种操作
- 把"是否需要提取"内置到了提取过程本身
- 事件结果
	- 成本下降，避免了大量无效写入，增量更新update，代替重写
```
ADD    ← 全新信息，之前没有  
UPDATE ← 已有记忆的值发生了变化（用户换了工作，更新职位信息）  
DELETE ← 已有记忆过时或被否定（用户说"我已经不用 mock 了"）  
NOOP   ← 没有值得记的新信息，不做任何操作
```


### 上述策略对比

|维度|Claude Code|Generative Agents|MemGPT|Mem0|
|---|---|---|---|---|
|触发方式|数量阈值（≥4条新消息）|重要性积分（≥150）|LLM 自主判断|每轮触发+NOOP过滤|
|触发确定性|确定性|确定性|非确定性|确定性|
|与主对话关系|完全解耦（后台异步）|写入同步，反思异步|耦合（函数调用）|可解耦|
|并发控制|Coalescing|无（单 Agent）|无（LLM 自管理）|依实现|
|防无效提取|数量门槛|重要性积分门槛|LLM 判断|NOOP 操作|
|适用场景|代码辅助/长期工具|角色扮演/社交 Agent|批处理/上下文密集|生产级对话 Agent|

**适用场景**
- **实时对话 Agent（用户实时等待响应）：** 优先参考 Claude Code 的架构——后台 fire-and-forget 解耦，不阻塞主对话，Coalescing 防并发。触发阈值根据实际对话长度调整，不一定非得是 4。
- **角色扮演或社交 Agent（信息密度高，事件驱动）：** Generative Agents 的重要性积分更合适，能根据对话内容的实际价值动态调整提取频率。
- **批处理分析型 Agent（大量历史对话，不要求实时）：** Mem0 的 CRUD 模型更规范，增量更新代替全量重写，长期成本更低。

## 参考链接
- [整理](https://mp.weixin.qq.com/s/V3LBQYZBNGRku1vj2iB9bw)
