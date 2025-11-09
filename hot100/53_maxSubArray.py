# 最大子数组和  数组｜分治｜动态规划
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 1️⃣ DP implement
def maxSubArray_1(nums: list[int]) -> int:

    # 初始化状态
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1,len(nums)):

        # 决定是否继续之前的数组，还是从当前元素重新开始
        # 之前子数组的和若为正数，则继续累加；否则重新开始 📍
        current_sum = max(nums[i],current_sum+nums[i])  # 状态转移方程

        max_sum = max(max_sum,current_sum)

    return max_sum

# 2️⃣ TODO 分治实现
def maxSubArray(nums: list[int]) -> int:

    pass

# 测试用例
if __name__ == "__main__":
    # 示例 1
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    print(f"输入: {nums1}")
    print(f"输出: {maxSubArray(nums1)}")  # 期望输出: 6
    
    # 示例 2
    nums2 = [1]
    print(f"输入: {nums2}")
    print(f"输出: {maxSubArray(nums2)}")  # 期望输出: 1
    
    # 示例 3
    nums3 = [5,4,-1,7,8]
    print(f"输入: {nums3}")
    print(f"输出: {maxSubArray(nums3)}")  # 期望输出: 23