# 给出2个单链表头结点，返回两个单链表相交的起始节点

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        双指针解法（时间 O(m+n)，空间 O(1)）

        核心想法：
        - pa 先走链表 A，再走链表 B
        - pb 先走链表 B，再走链表 A
        这样 pa 和 pb 走过的总长度相同，都会是 A+B。

        结果：
        - 有交点：两指针会在交点第一次相遇
        - 无交点：两指针最终都会变成 None，并在 None 处相遇
        """
        # pa、pb 分别从两个链表头出发
        pa, pb = headA, headB

        while pa is not pb:
            # pa 走到末尾(None)后，切换到 B 的头继续走
            pa = pa.next if pa else headB
            # pb 走到末尾(None)后，切换到 A 的头继续走
            pb = pb.next if pb else headA

        # 循环结束时：
        # - 要么 pa/pb 是交点节点
        # - 要么 pa/pb 都是 None（说明不相交）
        return pa