# 爬楼梯
def climbStairs(n):

    ## 递归实现 O(2^n) 存在大量重复计算
    # if n<=2:
    #     return n
    # return climbStairs(n-1)+climbStairs(n-2)


    ## 动态规划实现 O(n)
    if n<=2:
        return n
    # 基础状态
    prev2=1 #到达第 1 阶，1 种，后续表示 i-2
    prev1=2 #到达第 2 阶，1 种，后续表示 i-1
    for i in range(3,n+1):
        current=prev2+prev1 # 到达第 i 阶的方法
        prev2=prev1
        prev1=current
    return prev1

if __name__ == "__main__":
    print(climbStairs(300))