### 4 寻找两个正序数组的中位数_high

【题意】
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。
——简言之，寻找两个有序数组合并后的，中位数。但时间复杂度有要求

【Code】

().[4_find_Median_SortedArrays.py]


【方法】
**思路**

1. 问题本质：寻找一个==分割线==，使得num1和num2 左侧的元素均小于等于右侧的元素
   1. 总的左侧与右侧元素数相等。因此，在num1中确定分割线后，num2中直接会有对应分割线
2. 建立二分查找模型
   1. num1，num2分别有m,n个元素
   2. 在i处分割，i一定为整数
      1. num1，左侧 `nums1[0], ..., nums1[i-1]` (共 i 个元素)；右边部分：`nums1[i], ..., nums1[m-1]` （m-i个元素）
      2. 为了满足分割线要求，num2会存在对应位置的割线 j ` i + j = (m + n + 1) // 2`
         1. m+n为偶数，则i+j=(m+n)/2，中位数需要是左右的平均值
         2. m+n为奇数，则i+j比剩余部分大一，中位数为左侧最大值
3. 正确分割条件 ` max(L1, L2) <= min(R1, R2)` ==正确条件==
   1. 简化，等价为 （因为原本）
      1. `nums1[i-1] <= nums2[j]`
      2. `nums2[j-1] <= nums1[i]`
4. 二分查找调整策略
   1. i偏小,需要右移，表现 `nums2[j-1] > nums1[i]`
   2. i偏大，需要左移，表现 `nums1[i-1] > nums2[j]`
5. 正确结果
   1. 与二分查找模型对应 (左侧数目等于右侧 或左侧大一)
   2. 偶数时， `(max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j])) / 2`
   3. 奇数时，`max(nums1[i-1], nums2[j-1])`

💡本质，寻找分割线，使得左右大小满足，计算中位数

**实现**

```python
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2): # 优化，使得二分查找在较短数组上执行
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
			
        total_left =(m+n+1)//2 # 1️⃣

        left,right=0,m

        while left<=right:
            i=(left+right)//2 # 调整i，寻找分界点
            j=total_left - i

            # 处理四个关键值 注意索引边界值 2️⃣
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
```

问题1：
 `+1` 是一个非常巧妙的设计，目的是**统一处理总长度为奇数和偶数两种情况**
 不用使用，if-else判断奇偶
 
问题2：为什么引入正无穷
简言之为了，处理索引越界

- **`i = 0`** 时， `nums1[i-1]` (即 `nums1[-1]`) 会导致索引越界，使用 `float('-inf')` 作为 `nums1_left_max`的占位符
  - 从而不影响 `max(nums1_left_max, nums2_left_max)` 的结果
- `i = m` 时，`nums1[i]` (即 `nums1[m]`) 会导致索引越界，使用float('inf')，作为num1_right_min的占位符
  - 从而不影响 `min(nums1_right_min, nums2_right_min)` 的结果
- `j=0` 和 `j=n` 的情况同理
