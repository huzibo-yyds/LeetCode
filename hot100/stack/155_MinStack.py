# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。


class MinStack:
    def __init__(self):
        """
        使用一个主栈 stack 和一个辅助栈 min_stack
        - stack: 正常存储所有元素
        - min_stack: 栈顶始终保存当前 stack 中的最小值
        """
        self.stack=[]
        self.min_stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            # 只有当 min_stack 为空，或新元素小于等于当前最小值
            # 等于，情况也需要加
            self.min_stack.append(val)
        
    def pop(self) -> None:
        popped_val = self.stack.pop()
        if popped_val==self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return  self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
