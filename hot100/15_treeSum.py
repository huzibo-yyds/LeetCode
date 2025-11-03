# 三数之和
# 返回和为0，结果三元组不能重复
def threeSum(nums: list[int]) -> list[list[int]]:
    """
    找出所有和为0的不重复三元组
    
    Args:
        nums: 整数数组
    
    Returns:
        所有和为0的不重复三元组列表
    """
    nums.sort() #📍排序、方便使用双指针和去重
    result = []
    n = len(nums)

    # loop1: 固定第一个数，转换为双指针问题
    for i in range(n-2):
        # 数组排序，若第一个数大于0，则后续均大于 0，无解
        if nums[i]>0:
            break
        
        # 冗余逻辑，避免重复三元组
        if i>0 and nums[i]==nums[i-1]:
            continue
        
        # 双指针——用于寻找另外两个数
        left= i+1
        right = n -1

        while left<right:
            total = nums[i]+nums[left]+nums[right]
            if total==0:
                result.append([nums[i],nums[left],nums[right]])

                # 去重，跳过相同元素避免结果重复
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1
                
                #移动指针继续寻找
                left+=1
                right-=1

            elif total<0:
                # 和小于0，需要数字变大，left 右移
                left+=1
            else:
                # 和大于0，需要变小，right做一
                right-=1
            
    return result



# 测试用例
if __name__ == "__main__":
    # 示例 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"输入: {nums1}")
    print(f"输出: {threeSum(nums1)}")  # 应该输出 [[-1,-1,2],[-1,0,1]]
    
    # 示例 2
    nums2 = [0, 1, 1]
    print(f"输入: {nums2}")
    print(f"输出: {threeSum(nums2)}")  # 应该输出 []
    
    # 示例 3
    nums3 = [0, 0, 0]
    print(f"输入: {nums3}")
    print(f"输出: {threeSum(nums3)}")  # 应该输出 [[0,0,0]]
    
    # 额外测试用例
    nums4 = [-2, 0, 1, 1, 2]
    print(f"输入: {nums4}")
    print(f"输出: {threeSum(nums4)}")  # 应该输出 [[-2,0,2],[-2,1,1]]