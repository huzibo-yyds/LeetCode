# 括号生成
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        l,r = 0,0 # 记录左右括号数量
        def backtrack(curr_str:str):
            nonlocal l,r
            if l==n and r==n:
                result.append(curr_str)

            # words=['('*(n-l),')'*l] #❌
            # words = ['('] * (n-l) + [')'] * (l-r) # ❗会产生重复结果

            words=[] # 最小化合法选择
            if l<n:
                words.append('(')
            if r<l:
                words.append(')')

            for word in words:
                if word == '(':
                    l+=1
                else:
                    r+=1
                
                # 1、2
                backtrack(curr_str+word)

                # 3 撤销选择
                if word == '(':
                    l-=1
                else:
                    r-=1

        
        backtrack('')
        return result
    
    def generateParenthesis_(self, n: int) -> list[str]:
        result = []
        
        # left 和 right 分别代表已使用的左括号和右括号的数量
        def backtrack(current_str: str, left: int, right: int):
            # 终止条件：当字符串长度达到 2*n 时，说明一个组合已完成
            if len(current_str) == 2 * n:
                result.append(current_str)
                return

            # 剪枝条件 1: 如果左括号数量还没达到 n，我们可以添加一个左括号
            if left < n:
                backtrack(current_str + '(', left + 1, right)

            # 剪枝条件 2: 如果右括号数量小于左括号数量，我们可以添加一个右括号
            # 这保证了括号组合的有效性
            if right < left:
                backtrack(current_str + ')', left, right + 1)

        # 初始调用，从一个空字符串，0个左括号，0个右括号开始
        backtrack('', 0, 0)
        return result
    

solution=Solution()
print(solution.generateParenthesis(2))