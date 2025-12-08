# 每日温度
# temperatures ，表示每天的温度
# 返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后

'''
输入: [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
'''

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        '''
        问题关键，对于一个温度，寻找右侧第一个比他大的数

        思路：单调栈
            这个占存储的是日期的索引
            从栈底到栈顶，存储的温度是单调递减的
        
        当新的温度，比栈顶高，则说明找到了更高的那天    
            弹出栈顶索引，当前索引-栈顶索引，即为天数差
            继续与新的栈顶对比，直到，栈为空或当前温度不比栈顶高
            将今天温度入栈
        
        最后栈中可能还剩余元素，他们不存在比起很高的温度，因此结果是0
        '''
        n=len(temperatures)
        answer = [0]*n
        stack=[]
        
        for i,temp in enumerate(temperatures):
            # 核心逻辑
            # 当栈不为空，当前温度大于栈顶元素，则找到结果
            while stack and temp>temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index]=i- prev_index # 计算天数差
            
            stack.append(i)

        return answer
