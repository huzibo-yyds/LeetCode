# 分割回文串
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

'''
所有可能    需要回溯系统性探索
分割        在字符串的每个位置面临是否分割的决策
回文串      检查子串

'''

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result=[]
        path=[]
        n =len(s)

        def is_palindrome(sub:str)-> bool:
            return sub == sub[::-1]
        
        def backtrack(star_index : int):
            '''
            从star_index开始寻找回文串
            '''

            # 终止条件，起始位置等于字符串长度
            if star_index==n:
                result.append(path[:])
                return
            
            # 遍历所有切割点
            for i in range (star_index,n):
                substring = s[star_index:i+1]

                if not is_palindrome(substring): # 剪枝
                    continue

                path.append(substring) # 1

                # 遍历所有长度子串的切割 
                backtrack(i+1) # 2 从 i + 1 位置继续往下切割

                path.pop() # 3回溯，开启更长字串的切割
        
        backtrack(0)
        return result
        
'''执行说明 ， readme文件
可以理解为树的分支
- 字串的左右都需要变，此外字串的长度也需要变📍
'''
        

