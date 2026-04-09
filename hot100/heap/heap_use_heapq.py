'''
使用 heaqp 实现常见堆操作
'''
import heapq


# 1) heappush / heappop / heap[0]
# Python 的 heapq 是基于 list 实现的小根堆。
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
print("after heappush:", heap)  # 这是堆的内部数组表示，不是完全有序数组
print("peek min (heap[0]):", heap[0])  # O(1) 读取堆顶最小值
print("heappop:", heapq.heappop(heap))  # O(log n) 弹出最小值
print("after heappop:", heap)
print("type(heap):", type(heap))  # 类型仍然是 list


# 2) heapify
# 把普通列表原地转换为合法的小根堆，时间复杂度 O(n)。
nums = [7, 2, 9, 1, 6]
heapq.heapify(nums)
print("after heapify:", nums)


# 3) heappushpop
# 先 push，再 pop，并返回弹出的最小值。
heap = [2, 4, 8]
heapq.heapify(heap)
result = heapq.heappushpop(heap, 3)
print("heappushpop returned:", result)
print("heap after heappushpop:", heap)


# 4) heapreplace
# 先 pop 最小值，再 push 新元素。
# 常用于固定大小堆的更新。
heap = [2, 4, 8]
heapq.heapify(heap)
result = heapq.heapreplace(heap, 3)
print("heapreplace returned:", result)
print("heap after heapreplace:", heap)


# 5) nsmallest / nlargest
arr = [5, 1, 9, 3, 7, 2]
print("nsmallest(3):", heapq.nsmallest(3, arr))
print("nlargest(2):", heapq.nlargest(2, arr))


# 6) merge
# 懒加载地合并多个已排序迭代器。
a = [1, 4, 7]
b = [2, 5, 8]
c = [3, 6, 9]
merged = list(heapq.merge(a, b, c))
print("merge:", merged)


# 7) 使用元组实现自定义优先级
# 元组比较规则：先比第 1 个元素，再比第 2 个元素。
tasks = []
heapq.heappush(tasks, (2, "low"))
heapq.heappush(tasks, (1, "high"))
heapq.heappush(tasks, (2, "low-2"))
print("task pop 1:", heapq.heappop(tasks))
print("task pop 2:", heapq.heappop(tasks))
print("task pop 3:", heapq.heappop(tasks))


# 8) Python 中模拟大根堆：存负数
max_heap = []
for x in [3, 1, 5]:
	heapq.heappush(max_heap, -x)
print("max value:", -heapq.heappop(max_heap))