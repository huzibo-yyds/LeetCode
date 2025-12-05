# 在排序数组中查找元素第一个和最后一个位置
# 数组中允许存在啊重复元素
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
# 若不存在目标值，则返回 [-1,-1]


class Solution:
    # 1️⃣ 我的实现
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left,right = 0,len(nums)-1

        def lookup_range(index:int)->list[int]:
            left,right=index,index
            for i in range(len(nums)):
                if left-1>=0 and nums[left-1]==target:
                    left=left-1
                elif right+1<=(len(nums)-1) and nums[right+1]==target:
                    right=right+1
                else:
                    break

            return [left,right]


        while left<=right:
            mid = left + (right- left)//2

            if nums[mid] == target:
                return lookup_range(mid)
            elif  target>nums[mid]:
                left=mid+1
            else:
                right=mid- 1

        return [-1,-1]
    

    # 📍面向对象编程中，函数是并列的，不存在前后书写的关系 

    # 2️⃣ 最推荐的写法，两次二分查找
    def find_bound(self,nums:list[int],target:int,is_left:bool)-> int:
        '''
        寻找 target 在 nums 中的左边界或右边界。
        is_left: True 表示寻找左边界，False 表示寻找右边界。
        '''
        left,right = 0,len(nums)-1
        bound=-1 # 使用bound来记录找到target的坐标
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                bound=mid   # 找到target，此数可以是满足要求中的任意一个
                # ❗ 改变问题规模
                # 在更小的列表中找target，直到找不到
                if is_left:
                    right=mid-1
                else:
                    left=mid+1
            elif  target>nums[mid]:
                left=mid+1
            else:
                right=mid- 1
            return bound
    
    def searchRange_opt(self, nums: list[int], target: int) -> list[int]:
        left_bound = self.find_bound(nums,target,True)

        if left_bound == -1:
            return [-1,-1]
        
        right_bound = self.find_bound(nums,target,False)
        return[left_bound,right_bound]


        
