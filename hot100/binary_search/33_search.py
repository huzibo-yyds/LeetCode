# 搜索旋转排序数组

# 💬 建议之，有序数组，旋转后，寻找target坐标
# 给你 旋转后的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

# 时间复杂度为 O(log n)


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        '''
        1、寻找数组中最小值的坐标，确定旋转点
        2、确定target在哪一侧搜索
            ❌使用数组获得排序好的原始nums
        3、在确定侧进行二分查找
        '''

        if not nums:
            return -1
        
        n = len(nums)
        left,right = 0,n-1

        # 1 寻找旋转点
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                # 右侧无序 最小值在mid右侧   [mid + 1, right] 
                left=mid+1
            else:
                # nums[mid] <= nums[right]): 这说明从 mid 到 right 这部分是有序的
                # 最小值在mid左侧或在mid 更新区间 [left, mid]
                right=mid  # 若while判断加等号的话，则此处无限循环

        prvot = left

        # 2 判断区间
        left,right = 0,n-1
        # if target>=nums[left]: # 🟥此处判断，在nums为[1]时失败
        #     right=prvot-1 #左侧
        # else:
        #     left=prvot
        if target>=nums[prvot] and target<=nums[right]: #⭐⭐ 此处判断条件在列表只有一个数时同样适用
            left=prvot
        else:
            right=prvot-1

        # 3 二分查找最终结果
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid - 1
            else:
                left=mid+1
        
        return -1
             