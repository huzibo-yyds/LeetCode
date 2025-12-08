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
