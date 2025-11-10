# 缺失的第一个正数
# 数组| 哈希


def firstMissingPositive(nums: list[int]) -> int:
    """
    找出未出现的最小正整数
    
    Args:
        nums: List[int] - 未排序的整数数组
    
    Returns:
        int - 缺失的最小正整数
    """
    nums.sort()
    n=len(nums)
    temp=1
    
    # - 没有正数的情况
    if nums[n-1]<=0:
        return 1

    i = 0
    while i<n:
        if nums[i]==temp:
            while i<n and nums[i]==temp: # - 从下往上寻找第一个缺失正数
                i+=1
            # 考虑重复temp
            temp+=1
        elif nums[i]>temp: # (1 正数未从1开始 (2 一般情况 
            return temp
        else:
            i+=1

    return temp

# 测试用例
if __name__ == "__main__":
    # 示例 1
    nums1 = [1, 2, 0]
    print(f"输入: {nums1}")
    print(f"输出: {firstMissingPositive(nums1)}")  # 期望输出: 3
    
    # 示例 2
    nums2 = [3, 4, -1, 1]
    print(f"输入: {nums2}")
    print(f"输出: {firstMissingPositive(nums2)}")  # 期望输出: 2
    
    # 示例 3
    nums3 = [7, 8, 9, 11, 12]
    print(f"输入: {nums3}")
    print(f"输出: {firstMissingPositive(nums3)}")  # 期望输出: 1

    nums4= [0]
    print(f"输入: {nums4}")
    print(f"输出: {firstMissingPositive(nums4)}")  # 期望输出: 1
    
    nums5= [1,2,3]
    print(f"输入: {nums5}")
    print(f"输出: {firstMissingPositive(nums5)}")  # 期望输出: 4