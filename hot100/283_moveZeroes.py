# 移动 0
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
# 📎双指针
def moveZeroes(nums: list[int]) -> None:
    """
    将数组中的所有0移动到末尾，保持非零元素的相对顺序
    使用双指针方法，原地修改数组
    
    Args:
        nums: 输入的整数数组
    
    Returns:
        None (原地修改)
    """    
    write = 0 # 写指针，下一个非0元素位置

    # loop1：将所有非0元素前移
    for read in range(len(nums)):
        if nums[read]!=0:
            nums[write]=nums[read] # 将非零元素前移
            write += 1

    # loop2：剩余位置填充为 0
    for i in range(write,len(nums)):
        nums[i]=0


# 测试用例
if __name__ == "__main__":
    # 示例 1
    nums1 = [0, 1, 0, 3, 12]
    print(f"输入: {nums1}")
    moveZeroes(nums1)
    print(f"输出: {nums1}")
    print(f"期望: [1, 3, 12, 0, 0]\n")
    
    # 示例 2
    nums2 = [0]
    print(f"输入: {nums2}")
    moveZeroes(nums2)
    print(f"输出: {nums2}")
    print(f"期望: [0]\n")
    
    # 额外测试用例
    nums3 = [1, 2, 3, 4]
    print(f"输入: {nums3}")
    moveZeroes(nums3)
    print(f"输出: {nums3}")
    print(f"期望: [1, 2, 3, 4]\n")
    
    nums4 = [0, 0, 1]
    print(f"输入: {nums4}")
    moveZeroes(nums4)
    print(f"输出: {nums4}")
    print(f"期望: [1, 0, 0]\n")