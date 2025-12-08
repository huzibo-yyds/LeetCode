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
