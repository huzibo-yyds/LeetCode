### 20 有效的括号_low

【题意】
给定一个只包括 `'('，')'，'{'，'}'，'['，']'` 的字符串 s ，判断字符串是否有效。
1、左括号必须用相同类型的右括号闭合。
2、左括号必须以正确的顺序闭合。
3、每个右括号都有一个对应的相同类型的左括号。

【code】

[20_isValid.py](20_isValid.py)

【方法】

1. 问题本质，*一个右括号总是与它左边最近的、未被匹配的那个左括号进行配对*
   1. 适合使用栈
2. 使用==列表==模拟栈、使用==哈希表(字典==)记录配对关系
   1. 键为，右括号
   2. 值为，左括号
3. 具体执行
   1. 遍历字符串
   2. 若遇到左括号，入栈
   3. 若遇到右括号，判断栈顶元素是否匹配
   4. 若遍历整个操作完成，栈为空，则说明字符串合法

【实现】

```python
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1: # 若长度为奇数则直接不用判断
            return False
    
        # 在python中使用list模拟栈
        stack = []
        # 配对关系的哈希表
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        # 📍 遍历每个元素进行判断
        for char in s:
            if char in pairs: # 右括号
                if not stack or stack.pop()!=pairs[char]:
                    return False
            else:   # 左括号
                stack.append(char)
                
        return not stack
```



### 155 最小栈

【题意】
设计一个支持 push ，pop ，top 操作，并能*在常数时间内检索到最小元素的栈。*
【code】

【方法】

- 难点，常数时间检测到最小值
  - 想到，拿空间换时间
- 解决
  - 在每次操作时就维护好当前的最小值
  - 添加额外的辅助栈 `min_stack`，栈顶保存当前 `self.stack`中的最小值
  - 随着stack，pop、push而更新

【实现】

```python
class MinStack:
    def __init__(self):
        """
        使用一个主栈 stack 和一个辅助栈 min_stack
        - stack: 正常存储所有元素
        - min_stack: 栈顶始终保存当前 stack 中的最小值
        """
        self.stack=[]
        self.min_stack = []
  
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            # 只有当 min_stack 为空，或新元素小于等于当前最小值
            # 等于，情况也需要加
            self.min_stack.append(val)
    
    def pop(self) -> None:
        popped_val = self.stack.pop()
        if popped_val==self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return  self.min_stack[-1]
```




### 394 字符串解码

【题意】
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: `k[encoded_string]`，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的

- 原始数据不包含数字
- 数字只表示重复次数

【code】

[394_decodeString.py](394_decodeString.py)

【方法】
本质，栈能完美处理“嵌套”具有“先进后出”的结构

1. 将 `[`看作进入一个更深层次的开始
2. 把 `]`看作当前层次的结束，并返回上一层
3. 当进入新层次时，保存上一层状态
4. 返回上一层的时候，将保存的状态恢复，并加上新层次的东西

【实现】

```python
class Solution:
    def decodeString(self, s: str) -> str:
        '''
        将[看作进入一个更深层次的开始
        把]看作当前层次的结束，并返回上一层
        当进入新层次时，保存上一层状态
        返回上一层的时候，将保存的状态恢复，并加上新层次的东西
        '''
        stack= []
        res= '' # 记录当前层解码的字符串
        multi=0
        for char in s:
            if '0'<= char <='9':
                multi = multi*10 + int(char) # 1️⃣ 处理数字
            elif char=='[':
                # 当前倍数，上一层字符串结果，入栈
                stack.append((multi,res))
                multi=0
                res=''
            elif char==']': #解码并更新res
                last_multi,last_res = stack.pop()
                res=last_res+last_multi*res # 执行解码，更新res
            else:
                res+=char # 记录当前层字符
        return res
```



### 739 每日温度

【题意】
每日温度
temperatures ，表示每天的温度
返回一个数组 answer ，其中 `answer[i]` 是指对于第 i 天，下一个更高温度出现在几天后

【code】

[739_dailyTemperatures.py](739_dailyTemperatures.py)

【方法】
**问题关键**，对于一个温度，寻找右侧第一个比他大的数

思路：==单调栈==
这个栈存储的是日期的索引
从栈底到栈顶，存储的温度是单调递减的

1. 对每天温度入栈
2. 当新的温度，比栈顶高，则说明找到了更高的那天1. 弹出栈顶索引，`当前索引-栈顶索引`，即为天数差
   2. 继续与新的栈顶对比，直到，栈为空或当前温度不比栈顶高
   3. 将今天温度入栈
3. 最后栈中可能还剩余元素，他们不存在比起很高的温度，因此结果是0

【实现】

```python
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        answer = [0]*n
        stack=[]
        for i,temp in enumerate(temperatures):
            # 核心逻辑
            # 当栈不为空，当前温度大于栈顶元素，则找到结果
            while stack and temp>temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index]=i- prev_index # 计算天数差
            stack.append(i)
        return answer
```
