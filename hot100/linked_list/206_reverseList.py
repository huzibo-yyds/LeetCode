# 给单链表的头结点，反转链表，并返回反转后的链表
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        迭代反转链表（时间 O(n)，空间 O(1)）
        最优解之一：必须遍历所有节点，因此时间下界是 O(n)。
        """
        # prev 指向已经反转好的前半部分，current 指向待处理节点
        prev = None
        current = head
        
        while current:  # 📍需要记录三个节点，前一个，当前，后一个
            # 保存下一个节点
            next_temp = current.next
            # 反转当前节点的指针
            current.next = prev
            # 移动指针
            prev = current
            current = next_temp
        
        # prev 是新链表的头
        return prev

    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归反转链表（时间 O(n)，空间 O(n) 递归栈）
        """
        # 空链表或单节点时，直接返回
        if not head or not head.next:
            return head

        # 反转后半部分，new_head 是反转后的头
        new_head = self.reverseList_recursive(head.next)
        # 将当前节点接到反转后的尾部
        head.next.next = head
        head.next = None
        return new_head