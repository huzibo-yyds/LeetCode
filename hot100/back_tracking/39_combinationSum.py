# 组合总和
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

# candidates 中的同一个数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        path=[]
        result = []

        def backtrack(curr_sum: int):
            if curr_sum==target:
                result.append(path[:])
                return
            
            if curr_sum>target:
                return

            # 📍 生成所有数字的全排列组合
            for num in candidates:
                path.append(num)
                backtrack(curr_sum+num)
                path.pop()
            
        
        backtrack(0)


        return result
    # ❌产生重复组合 [[2,2,3],[2,3,2],[3,2,2],[7]] 