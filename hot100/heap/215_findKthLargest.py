''' 数组中的第K个最大元素 '''
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        max_heap=[]
        for m in nums:
            heapq.heappush(max_heap,-m)
        
        i=0
        while i<k:
            n=heapq.heappop(max_heap)
            n=-n
            i+=1
        return n
