# 电话号码的字母组合

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        result= []
        dict={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        # 📍 增加index，追踪当前正在处理digits那个位置
        def backtrack(index: int, current_combination: str):
            if index==len(digits):
                result.append(current_combination)
                return
            
            letters = dict[digits[index]]

            for letter in letters:
                # 1、做选择，拼接letter
                # 2、进入下一个决策层
                backtrack(index+1, current_combination + letter)
                # 3、撤销选择（回溯），无需显式操作，因为current_combination是值传递
            

        backtrack(0, "")
        return result
