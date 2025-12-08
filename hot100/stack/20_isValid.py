# 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
'''
1、左括号必须用相同类型的右括号闭合。
2、左括号必须以正确的顺序闭合。
3、每个右括号都有一个对应的相同类型的左括号。
'''
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        本质：一个右括号总是与它左边最近的、未被匹配的那个左括号进行配对

        '''
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