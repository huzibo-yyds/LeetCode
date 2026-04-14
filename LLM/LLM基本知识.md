### LLM

### token

### Transformer

### 位置编码



### prefill & decode



### 注意力机制 attention
理解`attention`：序列中的每个 token，在编码自己时，会动态关注其他 token，对不同位置分配不同权重。

处理序列问题，传统做法 （如 *RNN*/*LSTM*）
- 信息必须从第一个词开始，传递到最后一个词
- 致命缺陷，句子很长的时候，信息在传递过程中*淡化*或*丢失*

> 在 Transformer 里，attention 被定义为：给定一个 query 和一组 key-value 对，先算 query 与各个 key 的匹配程度，再把这些匹配程度变成权重，最后对 value 做加权求和，得到输出。

📍 `attention机制`，Query, Key, Value (Q, K, V)
- Query (Q)：查询需求
- Key (K)：索引/标签
- Value (V) ：实际信息
*Q 决定“搜什么”，K 决定“匹不匹配”，V 决定“真正拿走什么内容”*
$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$
👆对公式的解释
1. 用当前token的Q与和所有token 的 K 做相似度计算
2. 得到一组分数，缩放因子 $\sqrt{d_k}$​​ 是为了避免点积过大
3. 经过softmax变成权重
4. 用权重对所有V加权求和


❓ attention改变了什么？
1. 打破了距离限制：词与词的关系不受距离影响
2. 实现了上下文感知：Context-Awareness
3. 并行计算：不用像RNN串行计算，Q、K、V可以在GPU上并行计算
与RNN/LSTM相比优势
4. 任意两个位置之间依赖路径更短
5. 更容易并行


`self-attention`：在当前序列内部，token与同一序列里其他token做关联，每个token生成三组向量

`为什么除以缩放因子` $\sqrt{d_k}$​​ 
因为如果 Q 和 K 的维度很大，点积值会变大，进入 softmax 后容易变得特别尖锐，导致梯度很小、训练不稳定。做缩放，可以缓解这个问题，*本质是为了训练稳定*。

`multi-head attention` **多头注意力机制**
把 Q、K、V 映射到多个子空间里，并行做多次 attention，再把结果拼起来。
- Transformer原文表述
	- 多头注意力允许模型在不同表示子空间、不同位置上，同时关注不同类型的信息；如果只用单头，容易被平均化。

### flash attention
`attention “效率瓶颈”` 背景
$\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$
- **计算流程**：$S=QK^T$  ，中间结果S（注意力权重矩阵）需要写会显存，再读出来进行softmax，再写会，再读出来乘以V
	- 随着序列长度增加，矩阵平方级增大
- **访存瓶颈**：访计算量虽然很大，但真正的瓶颈往往不在于计算本身，而在于频繁地在显存（HBM，高带宽显存）和处理器缓存（SRAM，高速片上缓存）之间搬运巨大的矩阵数据。
	- GPU内存模型可以简单分为2层
		- HBM：大，但相对慢 （标准attention，需要从HBM中频繁读写
		- 片上 SRAM / shared memory：小，但快

`FlashAttention`
- 是一种“精确的、IO-aware 的 attention 计算算法”。
- 通过 **tiling** 来减少 HBM 与片上 SRAM 之间的读写。
- **在不改变exact attention结果的前提下，使attention更适合GPU层次存储** 📍
> FlashAttention 优化的不是“attention 的定义”，而是“attention 在 GPU 上的实现方式”。

#### 为什么会提出flash attention❓
1. *长上下文* 会使标准attention，二次复杂度越来越大，显存和时间成本增加
2. 很多 *近似的attention* 方法，通过减少理论计算量，但不一定带来真的端到端加速
	1. 如sparse attention、low-rank attention。改变原始attion计算
3. 正在忽略的瓶颈是IO，而不是理论FLOPs（浮点运算次数）

#### `FA核心内容` ⭐️⭐️⭐️
分块（tiling） + 融合（fusion） + 在线 softmax（online softmax）

- 分块
	- 标准 attention 通常会把整个权重矩阵全部算出来。
	- 会把 Q、K、V 按块切开，一块一块地搬到片上 SRAM 里算。这样就不需要把完整的 N×N 注意力矩阵显式落到 HBM。
	- 即，*通过tiling 减少HBM和边上SRAM之间的读写次数*。

- 融合
	- 标准attention实现：1）计算权重矩阵 2）写会 3）读出执行softmax 4）写会 5）在读出成V
	- FA，将上面这些操作尽量融合在一个kernel中，减少中间结果落地到HBM的次数。
	- 减少读写，是FA变快的关键。

- 在线softmax
	- 标准softmax需要知道所有数据，而分tilie后如何做
	- 使用在线softmax，在逐块处理时，持续维护每一行的
		- 最大值 m、 归一化因子 l、 当前累计输出 O


> softmax: 将实数分布转换为概率分布
> $\operatorname{softmax}(x_i)=\frac{e^{x_i}}{\sum_j e^{x_j}}$  指数化 + 归一化 

#### FA快在哪里？为啥省？
- 减少中间大矩阵显式存储和HBM读写

📍（本质）
FlashAttention 的核心贡献不是把 attention 近似掉，而是在 exact attention 前提下，把内存访问模式做到了更高效，因此把实际运行效率大幅拉上去。

#### FA-2做了什么？
FlashAttention 已经解决了很多 IO 问题，但还没有把 GPU 的并行能力压榨到接近 GEMM。  
FlashAttention-2 论文指出，初代的不足主要来自 *thread block 和 warp 之间的工作划分不够好*，导致 occupancy 不高，或者 shared memory 里仍有不必要的读写。

它的三项主要改进是：
1. 减少非 matmul FLOPs
2. 对单个 head 也能跨多个 thread block 并行
3. 在 thread block 内更合理地分配 warp 工作，减少 shared memory 通信

#### FA常见问题
Q1：FlashAttention 是近似 attention 吗？
不是。它是 exact attention，也就是输出和标准 attention 数学上等价，只是计算方式变了。

Q2：它为什么快？
根本原因不是“减少了公式”，而是 减少了 HBM 读写，提升了 IO 效率。

Q3：它为什么能分块还保持 softmax 正确？
因为用了 *online softmax*，能在分块处理时持续维护归一化统计量。

Q4：它解决的是算力问题还是显存问题？
两者都改善，但最核心的切入点是 显存访问模式 / IO 问题。

Q5：它是不是把 attention 彻底变成线性复杂度？
更稳妥的说法是：它显著降低了 memory footprint 和 IO 成本，并带来实际加速；不要把它简单说成“把 exact dense attention 全部变成线性计算”。

### MOE

### 蒸馏

### Skill




---
### 上下文窗口 context window
- 理解为**大模型的短期记忆容量 或 模型的注意力视界**
- 在技术层面上，Context Window 指的是模型在处理当前请求时，能够同时“看到”并“处理”的 Token（字符/词元）总数。这包括了（三部分）：
	1. 你当前输入的指令（Prompt）。
	2. 你之前对话的历史记录（Chat History）。
	3. 模型正在生成的回答（Output）。

- 🟥 上下文窗口越大越好么？
	- 答：并**不是越大越好**，它存在“收益递减”和“成本激增”的边界
	- 更大的窗口带来的挑战
		- 注意力机制，计算复杂度是序列长度的平方倍 $O(N^2)$
			- 窗口增大10倍，计算量和显存占用增大100倍
		- 窗口增大，注意力涣散。模型往往能记住文本开头和结尾，但容易忽略文本中间信息
		- 响应延迟，latency增大。

有效上下文= 上下文窗口规模 × 检索精度 (Needle-in-a-Haystack Score)


KV cache、
batching、
吞吐、
延迟、
并发、
成本优化。
### 量化 Quantization
- 核心概念：**用“低精度”的数字去近似“高精度”的数字**。
	- 将 FP16（16位浮点数）或 FP32（32位浮点数）转换成 INT8（8位整数）甚至 INT4（4位整数）。
- 量化模型与原模型的区别？
	- 数值范围和进去额度，减少
	- 存储空间，减少
	- 计算速度，加快 （CPU、GPU处理整数，比浮点数快得多）
	- 占用的显存/内存带宽更小
- 对量化损失精度如何理解？
	- 模型本身存在信息冗余，参数微小变动，对接过影响不大
	- 鲁棒性：模型本身具有容错能力，量化后和原先的概率分布基本一致即可
	- 量化技术加持： GPTQ, AWQ, GGUF
- 本质上是一个trade-off
	- 部署可行性=推理速度×模型规模​ / 硬件成本×精度损失
	- 本质：牺牲一点点精度，换取逻辑上的可用性

|维度|追求量化 (Low Precision)|追求原模型 (High Precision)|
|---|---|---|
|准确性 (Accuracy)|略有下降 (Perplexity 升高)|最高 (Golden Standard)|
|显存占用 (VRAM)|极低 (可以在手机/普通电脑运行)|极高 (需要昂贵的 A100/H100 集群)|
|推理速度 (Latency)|极快 (响应即时)|较慢 (计算压力大)|



### LLM中常见算子


### RAG

### AI agent


### Agent设计

单智能体、多智能体、workflow orchestration、planning、memory、reflection、handoff。


什么时候需要agent，什么时候不需要
