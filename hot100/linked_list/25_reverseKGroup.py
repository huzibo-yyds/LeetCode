# K个一组翻转链表

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseList(self,head:Optional[ListNode]) -> Optional[ListNode]:
        ''' 迭代法翻转链表 '''
        prev=None
        current = head

        while current:
            next_temp=current.next
            current.next=prev
            prev=current
            current=next_temp
        
        return prev


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or not head:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 找到当前这一组的第 k 个节点（组尾）
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth: # 剩余不足k直接返回
                    return dummy.next

            group_next = kth.next

            # 原地反转当前组：[group_prev.next, kth]
            prev = group_next
            curr = group_prev.next
            while curr is not group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # 重新接回：group_prev -> 新组头(kth)，并更新 group_prev 到新组尾
            old_group_head = group_prev.next
            group_prev.next = kth
            group_prev = old_group_head

    '''
    1️⃣ group_prev
    2️⃣ group_next
    
    '''