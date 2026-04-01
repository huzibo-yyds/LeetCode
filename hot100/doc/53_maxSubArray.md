https://leetcode.cn/problems/maximum-subarray/

🔗 [[../learning/动态规划|动态规划]]

给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
**子数组**是数组中的一个连续部分。


## 解题思路


### 动态规划
核心思想
1. 定义状态
2. 创建状态转移方程

**状态**
我们用 f(i) 代表以第 i 个数结尾的「连续子数组的最大和」，那么很显然我们要求的答案就是：
$max_{(0≤i≤n−1）}​{f(i)}$

- 求出每个位置的 f(i) ，最后返回最大的 f(i)
- 如何求 f(i)
	- f(i) 取决于f(i-1)和 `nums[i]` ，因此得到**状态转移方程**
- $f(i)=max{f(i−1)+nums[i],nums[i]}$

复杂度分析
- 时间，O(n) ： 只需要便利一遍数组
- 空间，O(1)：需要额外的变量来存储当前最大与全局最大

#### code
```python
def maxSubArray(nums: list[int]) -> int:

    # 初始化状态
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1,len(nums)):

        # 决定是否继续之前的数组，还是从当前元素重新开始
        # 之前子数组的和若为正数，则继续累加；否则重新开始 📍
        current_sum = max(nums[i],current_sum+nums[i])  # 状态转移方程

        max_sum = max(max_sum,current_sum)

    return max_sum
```


### 分治
