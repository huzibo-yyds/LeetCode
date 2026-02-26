# 删除链表倒数第n个节点，返回头结点
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 虚拟头结点，统一处理删除头节点的情况
        dummy = ListNode(0, head)
        fast = slow = dummy

        # fast 先走 n 步，和 slow 拉开 n 的距离
        for _ in range(n):
            fast = fast.next

        # fast 和 slow 同时走，直到 fast 到达尾节点
        while fast.next:
            fast = fast.next
            slow = slow.next

        # 此时 slow.next 就是倒数第 n 个节点，执行删除
        slow.next = slow.next.next

        return dummy.next
