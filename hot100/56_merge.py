# 合并区间 ｜合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

# ❌尝试 1
def merge_x1(intervals: list[list[int]]) -> list[list[int]]:

    # 对子列表排序
    intervals.sort(key=lambda x:x[0])
    merged=[]

    for i in range(len(intervals)):

        j=i
        while intervals[j][1]>=intervals[j+1][0]:
            if j+1 >= len(intervals):
                break
            j+=1
        if j>i:
            merged.append([intervals[i][0],intervals[j][1]])
            i=j  # ❌ 此处 i 修改不生效
        else:
            merged.append([intervals[i][0],intervals[i][1]])

    return merged

def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x:x[0])
    merged = []

    i=0
    while i < len(intervals):
        
        # 记录当前区间起始结束
        start = intervals[i][0]
        end = intervals[i][1]

        # 判断是否有可合并区间
        j=i+1
        while j <len(intervals) and intervals[j][0]<=end: #后一个区间开始<=上一个区间结束
            end = max(end,intervals[j][1])
            j+=1
        
        merged.append([start,end])
        i = j # 📍 此处更新 i 在整个 while 循环中生效

    return merged
    

# 测试代码
if __name__ == "__main__":
    # 示例 1
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(f"输入: {intervals1}")
    result1 = merge(intervals1)
    print(f"输出: {result1}")
    print(f"预期: [[1,6],[8,10],[15,18]]\n")
    
    # 示例 2
    intervals2 = [[1,4],[4,5]]
    print(f"输入: {intervals2}")
    result2 = merge(intervals2)
    print(f"输出: {result2}")
    print(f"预期: [[1,5]]\n")
    
    # 示例 3
    intervals3 = [[4,7],[1,4]]
    print(f"输入: {intervals3}")
    result3 = merge(intervals3)
    print(f"输出: {result3}")
    print(f"预期: [[1,7]]\n")
    
    # 额外测试用例
    # 空列表
    intervals4 = []
    print(f"输入: {intervals4}")
    result4 = merge(intervals4)
    print(f"输出: {result4}")
    print(f"预期: []\n")
    
    # 单个区间
    intervals5 = [[1,3]]
    print(f"输入: {intervals5}")
    result5 = merge(intervals5)
    print(f"输出: {result5}")
    print(f"预期: [[1,3]]\n")
    
    # 多个重叠区间
    intervals6 = [[1,4],[2,3],[3,5],[6,8],[7,9]]
    print(f"输入: {intervals6}")
    result6 = merge(intervals6)
    print(f"输出: {result6}")
    print(f"预期: [[1,5],[6,9]]\n")