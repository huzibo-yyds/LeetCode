# 组合总和
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

# candidates 中的同一个数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        '''
        单调递增，全元素组合排列，允许重复元素
        '''
        path=[]
        result = []

        # 增加 start_index 避免重复组合
        def backtrack(start_index: int,curr_sum: int):
            if curr_sum==target:
                result.append(path[:])
                return
            
            if curr_sum>target:
                return

            # 📍 生成所有数字的全排列组合
            for i in range(start_index,len(candidates)):
                num=candidates[i]
                # 深搜三个关键步骤 
                path.append(num)
                backtrack(i,curr_sum+num) # 使用i确保能重复利用，但不会出现,如 [2,2,3],[2,3,2]的重复组合，只能单调递增
                path.pop()
            
        
        backtrack(0,0)


        return result
    # ❌产生重复组合 [[2,2,3],[2,3,2],[3,2,2],[7]] 
    # ✅start_index解决

    # 优化：可以先对 candidates 排序，这样剪枝可以更早触发
    def combinationSum_optimized(self, candidates: list[int], target: int) -> list[list[int]]:
        path = []
        result = []
        candidates.sort() # 排序

        def backtrack(start_index: int, current_sum: int):
            if current_sum == target:
                result.append(path[:])
                return

            for i in range(start_index, len(candidates)):
                num = candidates[i]
                
                # 优化剪枝：如果当前和加上 num 就超过了 target，
                # 因为数组已排序，后续的数字只会更大，所以可以直接 break 循环
                if current_sum + num > target:
                    break

                path.append(num)
                backtrack(i, current_sum + num)
                path.pop()
        
        backtrack(0, 0)
        return result