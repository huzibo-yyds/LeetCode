# 环形链表2，判断是否有环，并且，返回环开始的节点

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 背诵口诀：快慢同起点，快二慢一圈内见。
        # 相遇别急返，头指针与相遇点同速前。
        # 再次相遇处，就是入环点。
        """
        Floyd 快慢指针（龟兔赛跑）

        目标：若有环，返回环的入口节点；若无环，返回 None。
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        # 第 1 阶段：判断是否有环，并在环内找到第一次相遇点
        slow = fast = head

        while fast and fast.next:
            # slow 一次走 1 步，fast 一次走 2 步
            slow = slow.next
            fast = fast.next.next

            # 有环时，快慢指针一定会在环内相遇
            if slow is fast:
                # 第 2 阶段：从头节点和相遇点同时出发，二者每次都走 1 步
                # 首次相遇的位置就是环入口
                headA, headB = head, slow

                while headA is not headB:
                    headA = headA.next
                    headB = headB.next

                # 返回环入口
                return headA

        # fast 走到 None，说明无环
        return None
