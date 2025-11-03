# 盛最多水的容器
# 🔗 双指针 ｜ 贪心
# 简言之，横轴长度 x 两边较低高度

def maxArea(height: list[int]) -> int:

    left = 0
    right = len(height)-1
    max_water = 0

    while left < right:
        current_water = min(height[left],height[right])* (right-left)

        max_water = max(current_water,max_water)

        # 🟥 如何确定左右两个指针的移动（移动较小的
        # 面积： 两个指针指向的数字中较小值∗指针之间的距离 
        '''
            - 移动较大的，结果只会比现在更小，而且破坏了面积的上限
            - 移动较小的，结果可能会变大、变小
        '''
        if height[left]<height[right]:
            left+=1
        else:
            right-=1

    return max_water

# 测试用例
if __name__ == "__main__":
    # 示例 1
    height1 = [1,8,6,2,5,4,8,3,7]
    print(f"输入: {height1}")
    print(f"输出: {maxArea(height1)}")  # 应该输出 49
    
    # 示例 2
    height2 = [1,1]
    print(f"输入: {height2}")
    print(f"输出: {maxArea(height2)}")  # 应该输出 1