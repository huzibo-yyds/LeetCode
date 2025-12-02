# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result =[] # 存储结果
        path = [] # 当前构造的队列
        used = [False]*len(nums) # 标记数字是否使用

        def backtrack():

            # 递归终止条件
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range (len(nums)):
                if used[i]:
                    continue

                # 1 做选择
                path.append(nums[i])
                used[i] = True
                
                # 2 进入下一个决策层
                backtrack()

                # 3 撤销选择（回溯） 和递归之前完全相同的反向操作
                path.pop()
                used[i] = False
            
        backtrack()
        return result
