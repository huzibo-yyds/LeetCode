# 寻找两个正序数组的中位数
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

# 算法的时间复杂度应该为 O(log (m+n)) 。

'''🟥
1、时间复杂度如何满足 O(log (m+n))
2、两个数组分别有序，如何合并？

'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        '''💡
        1、寻找分割线，找到这样一条“分割线”，它能同时把 nums1 和 nums2 切开，形成合并后的“左半部分”和“右半部分”。
            左、右数量相等
        2、建立二分查找模型

        3、正确分割条件
            nums1 的左边 (L1)：nums1[i-1] 是其最大值
            nums1 的右边 (R1)：nums1[i] 是其最小值
            nums2 的左边 (L2)：nums2[j-1] 是其最大值
            nums2 的右边 (R2)：nums2[j] 是其最小值
            成功条件：总左边的最大值 <= 总右边的最大值
            max(L1, L2) <= min(R1, R2)
        
        4、二分查找调整策略
            i偏小
            i偏大
        5、最终中位数计算
        '''

        if len(nums1) > len(nums2):
            nums1,nums2=nums2,nums1

        m,n=len(nums1),len(nums2)
        
        # 合并后数组左半部分元素数目，奇数情况左侧大1
        total_left =(m+n+1)//2


        left,right=0,m

        while left<=right:
            i=(left+right)//2 # 调整i，寻找分界点
            j=total_left - i


            # 处理四个关键值 注意索引边界值📍
            # 如果 i=0, nums1_left_max 不存在，设为负无穷
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            # 如果 i=m, nums1_right_min 不存在，设为正无穷
            nums1_right_min = float('inf') if i == m else nums1[i]
            # 同理处理 nums2
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            # 四个关键值判断
            if nums1_left_max<=nums2_right_min and nums2_left_max<=nums1_right_min:
                # 成功条件
                left_max=max(nums1_left_max,nums2_left_max)
                if (m+n)%2==1:
                    return left_max # 总长度为奇数
                else:
                    right_min=min(nums1_right_min,nums2_right_min)
                    return (left_max+right_min)/2.0  # 总长度为偶数
            elif nums1_left_max>nums2_right_min: # i 需要左移
                right=i-1
            else: #i需要右移 nums2_left_max >nums1_right_min
                left=i+1
            
        return -1
