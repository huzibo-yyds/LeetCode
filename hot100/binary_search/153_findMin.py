# 寻找旋转排序数组中的最小值

# 📍 与leetcode 33类似

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n=len(nums)
        left,right = 0,n-1

        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]: #
                left=mid+1
            else:
                right=mid
        
        return nums[right]