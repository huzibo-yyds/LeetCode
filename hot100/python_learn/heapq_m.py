import heapq as hq
import numpy as np

data= np.arange(10)
print(data) # [0 1 2 3 4 5 6 7 8 9]
np.random.shuffle(data)
print(data) # [8 9 6 4 7 3 2 5 1 0]

heap=[]
for i in data:
    hq.heappush(heap,i)
print(heap) # [0, 1, 3, 5, 2, 8, 4, 9, 6, 7]

## 弹出堆中最小元素
hq.heappush(heap,0.5) 
print(heap) # [0, 0.5, 3, 5, 1, 8, 4, 9, 6, 7, 2]
print(hq.heappop(heap)) # 0
## 弹出最小元素，然后使用n替换
hq.heapreplace(heap,0) 
## 先push 再pop
hq.heappushpop(heap,-1)
print(heap)
## 返回最大的、最小的n个数
print(hq.nlargest(2,heap)) # [9, 8]
print(hq.nsmallest(2,heap)) # [0, 1]




## 将heap属性应用到任意一个列表
nums=[23,3,4,6]
hq.heapify(nums) 
print(nums)