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

# 示例参考
def firstMissingPositive_ck(nums: list[int]) -> int:
    '''
    1- 只关注有用的数，将有用的数放在正确的位置上
    2- 用数组当做哈希桶（原地哈希）
      操作中忽略，小于0，大于n，以及重复的数
    '''
    n= len(nums)

    # 1- 将正整数放到正确的位置 
    for i in range(n):
        while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
            correct_pos = nums[i]-1
            nums[i],nums[correct_pos]= nums[correct_pos],nums[i] #交换

    # 2- 找到第一个不在正确位置的数
    for i in range(n):
        if nums[i]!=i+1:
            return i+1
    
    return n+1
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