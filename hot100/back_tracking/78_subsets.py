# 子集  （46实现全排列）
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result =[] # 存储结果
        path = [] # 当前构造的队列

        def backtrack(start_index:int):
            # 每一步迭代均收集
            result.append(path[:]) # 🟥 path是一个可变对象直接使用得到的是引用，使用[:]得到的是一个拷贝

            if start_index>=len(nums):
                return
            
            # 📍遍历选择列表
            # 每个元素均存在使用和不使用两种情况
            for i in range (start_index,len(nums)):
                # 1 做选择
                path.append(nums[i])

                # 2 进入下一层决策
                backtrack(i+1)

                # 撤销决策
                path.pop()

        backtrack(0)
        return result