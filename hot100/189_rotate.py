# 轮转数组 （数组｜数学｜双指针）
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

def rotate(nums: list[int], k: int) -> list[int]:
    n= len(nums)
    k= k%n
    if k==0:
        return nums

    '''
    # 1- pop、insert
    # 时间复杂度是 O(k×n) ｜ 空间复杂度O(1)
    # for i in range(k):
    #     right=nums.pop()
    #     nums.insert(0,right) # 时间复杂度为O(n),需要在列表开始插入且将所有元素后移一位
    '''

    ''' 
    # 2 - 使用切片
    # 时间复杂度O(n) ｜ 空间复杂度O(1)
    nums[:]=nums[-k:] + nums[:-k]
    '''

    # ''' 3- 最优解：三次翻转
    def reverse(arr,start,end):
        while start<end:
            arr[start],arr[end] =arr[end],arr[start]
            start += 1
            end -= 1
    reverse(nums,0,n-1) # 第 1 次，翻转整个数组
    reverse(nums,0,k-1) # 第 2 次，翻转前k个元素
    reverse(nums,k,n-1) # 第 3 次，翻转后n-k个元素
    # '''

    return nums


# 测试代码
if __name__ == "__main__":
    # 测试用例 1
    nums1 = [1,2,3,4,5,6,7]
    k1 = 3
    print(rotate(nums1,k1))
    
    # 测试用例 2
    nums2 = [-1,-100,3,99]
    k2 = 2
    print(rotate(nums2,k2))