# 最长连续序列
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。    

def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    
    num_set = set(nums) # 去重
    longest = 0

    for num in num_set:
        # 📍关键点，减少时间复杂度
        # 只有当前面一个数不在集合中，才需要计算长度（这批数中后面任何数都没有第一个数的列表长度长）
        if num -1 not in num_set:
            current_num = num
            current_length = 1

            while current_num+1 in num_set:
                current_num += 1
                current_length += 1

            longest=max(longest,current_length)
    
    return longest
    


# 测试用例
if __name__ == "__main__":
    # 示例 1
    nums1 = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(nums1))  # 输出: 4
    
    # 示例 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longestConsecutive(nums2))  # 输出: 9
    
    # 示例 3
    nums3 = [1, 0, 1, 2]
    print(longestConsecutive(nums3))  # 输出: 3