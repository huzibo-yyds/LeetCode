
def twoSum(nums, target):
    """
    给定一个整数数组 nums 和一个目标值 target，
    请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

    示例:
    输入: nums = [2, 7, 11, 15], target = 9
    输出: [0, 1]
    解释: 因为 nums[0] + nums[1] = 2 + 7 = 9
    """
    num_to_index = {} # 创建一个字典(哈希表)，用于存储数字和索引
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    
    return []  # 如果没有找到符合条件的两个数


# 暴力枚举
def twoSum_baoli(nums:list[int],target:int) -> list[int]:
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]== target:
                return[i,j]
    return []

# 哈希表


# 测试代码
if __name__ == "__main__":
     # 测试用例
    nums = [2, 7, 11, 15]
    target = 9
    print(f"输入数组: {nums}")
    print(f"目标值: {target}")
    result = twoSum_baoli(nums, target)
    print(f"输出: {result}")  # 应该输出 [0, 1]
    
    # 额外测试用例
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"\n输入数组: {nums2}")
    print(f"目标值: {target2}")
    result2 = twoSum_baoli(nums2, target2)
    print(f"输出: {result2}")  # 应该输出 [1, 2]