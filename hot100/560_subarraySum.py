# 和为 k 的子数组

'''
方法 1：前缀和 + 暴力，超出时间限制
'''
def subarraySum_(nums: list[int], k: int) -> int:
    sum_i=[0]*len(nums)
    # nums.sort() # 子数组是数组中元素的连续非空序列。🟥 不需要排序
    num=0

    # 计算前缀和
    for i in range(len(nums)):
        if i==0:
            sum_i[i]=nums[i]
        else:
            sum_i[i]=sum_i[i-1]+nums[i]

        if sum_i[i]==k:
            num+=1

    # 判断区间内是否有
    for i in range(len(nums)):
        # if sum_i[i]<k:  # 🟥 未考虑到负数的情况
        #     continue
        j=0
        while j<i:
            if sum_i[i]-sum_i[j]==k:
                num+=1
            j+=1
    return num

def subarraySum(nums: list[int], k: int) -> int:
    n=len(nums)
    count = 0
    for i in range(n):
        sum = 0
        for j in range(i,-1,-1):  # 📍
            sum+=nums[j]
            if sum==k:
                count+=1
    return count
            

# 测试用例
if __name__ == "__main__":
    # 示例 1
    nums1 = [1, 1, 1]
    k1 = 2
    result1 = subarraySum(nums1, k1)
    print(f"输入: nums = {nums1}, k = {k1}")
    print(f"输出: {result1}")


    # 示例 2
    nums2 = [1, 2, 3]
    k2 = 3
    result2 = subarraySum(nums2, k2)
    print(f"输入: nums = {nums2}, k = {k2}")
    print(f"输出: {result2}")

    # 用例3
    nums3 = [1, 2, 1, 2, 1]
    k3 = 3
    result3 = subarraySum(nums3, k3)
    print(f"输入: nums = {nums3}, k = {k3}")
    print(f"输出: {result3}")

    # 用例4
    result4 =subarraySum([-1,-1,1],0)
    print(f"输出: {result4}")