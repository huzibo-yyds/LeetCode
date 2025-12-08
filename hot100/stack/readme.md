### 模板

最常见的两类问题

#### 配对消除

- 20，括号匹配
- 394，嵌套 先进先出

*核心思想*
这类问题的本质是处理成对出现的元素，当一个“结束”符号出现时，需要与离它**最近**的一个“开始”符号进行匹配和抵消。

*问题特征*

- 问题中存在**成对**的、需要**匹配**的元素。
- 匹配规则具有**就近原则**，即一个结束符号总是匹配最近的那个未被匹配的开始符号。
- 常常涉及**合法性校验**（如括号是否合法）或**化简**（如消除冗余部分）。

*通用解题模板*

1. 初始化，栈、匹配关系哈希表
2. 遇到开始符号，入栈
3. 遇到结束符号，判断是否匹配

```python
def pairing_elimination_template(sequence):
    stack = []
    # mapping = { 'end_symbol': 'start_symbol' } # 可选的配对关系

    for element in sequence:
        if is_start_symbol(element):
            # 1. 遇到“开始”符号，一律入栈
            stack.append(element)
        elif is_end_symbol(element):
            # 2. 遇到“结束”符号，进行判断
            # a. 如果栈为空，说明没有匹配的开始符号，无效
            if not stack:
                return False # or handle as invalid
          
            # b. 弹出栈顶的“开始”符号
            start_symbol = stack.pop()

            # c. 检查是否匹配
            if not is_match(start_symbol, element):
                return False # or handle as invalid
  
    # 3. 遍历结束后，如果栈为空，说明所有符号都完美配对
    return not stack
```

#### 单调栈

- 155，最小栈
- 739，每日温度

*核心思想*
单调栈是一种特殊的栈，它在操作过程中始终保持栈内元素的**单调性**（单调递增或单调递减）。它的主要作用是高效地找到一个元素**左边或右边第一个比它大/小**的元素。

*核心机制*
当一个新元素将要入栈时，为了维持栈的单调性，我们会不断地将栈顶不符合单调性的元素弹出。**而这个弹出的时刻，就是我们找到答案的时刻！**

- 对于被弹出的元素 `stack.top()` 来说，新来的这个元素 `new_element` 就是它右边第一个破坏单调性（即第一个比它大/小）的元素。

*问题特征*

- 题目要求寻找每个元素**左/右侧**的**第一个**更大/更小的元素。
- 关键词：“下一个更大”、“上一个更小”、“最近的大于”等。
- 问题可以转化为求解每个元素与其左/右侧第一个关键元素之间的**距离**或**关系**。

*通用解法模板 (以“寻找右侧第一个更大”为例，递减栈)*

```python
def monotonic_stack_template(nums):
    n = len(nums)
    result = [-1] * n # 初始化结果数组
    stack = [] # 栈中存储的是元素的索引

    for i in range(n):
        # 1. 核心：当栈不为空，且当前元素大于栈顶索引对应的元素时
        while stack and nums[i] > nums[stack[-1]]:
            # 2. 找到了栈顶元素的“右侧第一个更大元素”
            top_index = stack.pop()
        
            # 3. 记录结果（可以是值，也可以是距离）
            result[top_index] = nums[i] # 或者 result[top_index] = i - top_index
    
        # 4. 将当前元素的索引入栈，维持单调性
        stack.append(i)
    
    return result
```


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
