# 柱状图中最大的矩阵
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        '''
        单调栈
        左边界- 由栈内小于当前元素的坐标决定（并不包含该值）
        右边界- 由当前遍历的元素决定
        '''
        heights=[0]+heights+[0]# 简化边界处理
        n = len(heights)
        stack = [] # 单调栈，从小到大
        max_area = 0

        for i in range(n):
            # 核心逻辑，当新的元素小于栈顶元素时，出栈计算面积
            # 💡此时面积不会稳定增大（当下一个元素大于栈顶元素时，面积为稳定增大）
            while stack and heights[i]<heights[stack[-1]]: #寻找面积的左右边界
                top_index = stack.pop()
                h = heights[top_index]

                left_boundary_index = stack[-1]

                w=i - left_boundary_index -1 # 左边界这一列并不算进来

                max_area=max(max_area,h*w)
            
            # 单调栈，每个元素均入栈
            stack.append(i) # 值为
        return max_area