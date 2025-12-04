# 搜索插入位置
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。（只需要位置，不需要真正插入）
# 请必须使用时间复杂度为 O(log n) 的算法。
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left,right = 0, len(nums)-1

        while left<=right:
            mid = left + (right- left)//2

            if nums[mid] == target:
                return mid
            elif  target>nums[mid]:
                left=mid+1
            else:
                right=mid- 1

        # 考虑不存在的情况
        # 最后一次 target>nums[mid] left会+1，插入位置就是 left
        # 最后一次 target<num[mid] ,应该在当前位置插入，即left位置

        return left
        