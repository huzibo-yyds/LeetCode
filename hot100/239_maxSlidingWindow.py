# 滑动窗口最大值

import heapq


def maxSlidingWindow_m(nums: list[int], k: int) -> list[int]:
    result=[]

    ''' 暴力法
    时间复杂度： O(NxK)，其中 N 是数组长度，K 是窗口大小

    📍 注意边界问题
        1- 在for循环中，从前往后遍历窗口 range(k,len(nums)+1),是不包含 len(nums)+1
        2- num[i-k:i] 是不包含i的
    '''
    for i in range(k,len(nums)+1): # 遍历所有
        window_max=max(nums[i-k:i]) #
        result.append(window_max)
    
    return result


# 优先队列(堆)
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    n=len(nums)
    # 创建初始窗口的堆，存储(-值, 索引)的元组
    q = [(-nums[i], i) for i in range(k)]
    heapq.heapify(q)  # 转换为堆结构 |使用元组第一个元素排序

    ans = [-q[0][0]]

    for i in range(k,n):
        heapq.heappush(q,(-nums[i],i))
        while q[0][1]<= i-k: # 若栈顶元素为过期元素，则移除，注意此处while
            heapq.heappop(q)
        ans.append(-q[0][0])

    return ans


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(maxSlidingWindow_m(nums,k)) # [3,3,5,5,6,7]
    print(maxSlidingWindow(nums,k)) # [3,3,5,5,6,7]