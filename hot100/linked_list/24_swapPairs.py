# 两两交换链表中的节点
# 你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
# 📍如果不限制必须节点交换，直接交换节点的 val 更简单

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        dummy + 局部指针重连

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        # dummy 统一处理头节点被交换的情况
        dummy = ListNode(0,head)
        # prev 指向“当前待交换这一对”的前一个节点
        prev = dummy

        # 至少还有两个节点时，才能执行一对交换
        while prev.next and prev.next.next:
            # a、b 是当前这一对节点：prev -> a -> b -> ...
            a = prev.next
            b = a.next

            # 执行交换（修改3条指向）（需要3个节点信息）
            a.next = b.next
            b.next = a
            prev.next = b

            # 交换后，a 成为这一对的尾巴；prev 后移到 a
            prev = a
        
        # 返回真实头节点
        return dummy.next