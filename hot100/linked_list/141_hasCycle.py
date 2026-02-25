# 环形链表，给定链表头结点，判断链表中是否有环

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        快慢指针法（Floyd的龟兔赛跑算法）
        
        时间复杂度：O(n)，最多遍历整个链表
        空间复杂度：O(1)，仅使用两个指针
        
        算法原理：
        - 若链表无环，fast 会先到达 None
        - 若链表有环，slow 和 fast 必然会在环内相遇
          原因：fast 每轮比 slow 多走一步，相当于在环内追赶 slow，必然相遇
        '''
        # 双指针同时从头出发
        slow = fast = head
        
        # 无环链表时 fast 会到达 None
        while fast and fast.next:
            # slow 一次走一步
            slow = slow.next
            # fast 一次走两步
            fast = fast.next.next
            # 两指针在环内相遇
            if slow is fast:
                return True
        
        # 没有相遇说明无环
        return False
            
