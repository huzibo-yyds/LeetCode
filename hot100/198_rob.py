# 打家劫舍

def rob(nums: list[int])->int:
    """
    计算能够偷窃到的最高金额
    
    Args:
        nums: List[int] - 每个房屋存放金额的数组
    
    Returns:
        int - 能够偷窃到的最高金额
    """
    if not nums:
        return 0
    if len(nums)==1:
        return nums[0]
    
    # dp[i] 表示到第 i 个房屋时能偷到的最高金额   1️⃣ 定义状态
    # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    # 即：要么不偷当前房屋（dp[i-1]），要么偷当前房屋（dp[i-2] + nums[i] 2️⃣ 状态转移方程

    prev2=nums[0] #
    prev1=max(nums[0],nums[1])
    if len(nums)==2:
        return prev1
    
    for i in range(2,len(nums)):
        current= max(prev1,prev2+nums[i])
        prev2=prev1
        prev1=current

    return prev1

# 测试代码
if __name__ == "__main__":
    # 示例 1
    assert rob([1, 2, 3, 1]) == 4
    # 示例 2
    assert rob([2, 7, 9, 3, 1]) == 12
    print("所有测试通过")
