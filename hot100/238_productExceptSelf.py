# 除自身以外数组的乘积
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
# 不要使用除法

def productExceptSelf(nums: list[int]) -> list[int]:
    
    left=1
    right=1
    n=len(nums)
    result=[1]*n

    for i in range(n-1):
        right*=nums[i+1]
    
    for i in range(n):
        result[i]=left * right
        left=left*nums[i]
        if i+1<n:
            if nums[i+1]!=0:
                right=right/nums[i+1] # 🟥违反了除法
            else:
                right=0
    
    return result

def productExceptSelf_a(nums: list[int]) -> list[int]:
    n=len(nums)
    result=[1]*n

    # 从左往右，计算左侧所有元素乘积 ｜ 前缀乘积
    left=1
    for i in range(n):
        result[i] = left
        left*=nums[i]
    
    # 从右往左，计算右侧所有元素乘积 ｜后缀乘积
    right=1
    for i in range(n-1,-1,-1): # 注意 range
        result[i]*=right
        right*=nums[i]
    
    return result


# 测试代码
if __name__ == "__main__":
    # 测试用例 1
    nums1 = [1,2,3,4]
    print(productExceptSelf_a(nums1))
    
    # 测试用例 2
    nums2 = [-1,1,0,-3,3]
    print(productExceptSelf_a(nums2))