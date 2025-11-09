# 接雨水
def trap_(height: list[int]) -> int:
    right=1
    water=0
    n= len(height)

    for i in range(n-1):
        if height[right]>=height[i]:
            # 若右侧与初始位置一样或者高于初始位置，无解
            if right<n-2:
                right+=1
            continue
        
        while height[right]<height[i]:
            water+=height[i]-height[right]
            right+=1
        
        i=right


    return water

# ----------------------------------------------
def trap(height: list[int]) -> int:
    if not height or len(height)<3:
        return 0
    
    # 双指针所需变量
    left,right = 0,len(height)-1
    left_max,right_max=0,0
    water = 0
    # 使用双指针向中间移动
    while left<right:
        left_max=max(left_max,height[left])
        right_max=max(right_max,height[right])

        # 根据较小一侧确定移动方向
        if left_max<right_max:
            water+=left_max-height[left]
            left+=1
        else:
            water+=right_max - height[right]
            right-=1
    return water


# 测试用例
if __name__ == "__main__":
    # 示例 1
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"输入: {height1}")
    print(f"输出: {trap(height1)}")  # 应该输出 6 # _m 错误输出为 0
    
    # 示例 2
    height2 = [4,2,0,3,2,5]
    print(f"输入: {height2}")
    print(f"输出: {trap(height2)}")  # 应该输出 9
    
    # 额外测试用例
    height3 = [3,0,2,0,4]
    print(f"输入: {height3}")
    print(f"输出: {trap(height3)}")  # 应该输出 7
    
    # 边界情况
    height4 = [1]
    print(f"输入: {height4}")
    print(f"输出: {trap(height4)}")  # 应该输出 0