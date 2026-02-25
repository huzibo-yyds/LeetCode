# 合并2个有序链表

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        head=ListNode()
        if list1.val<=list2.val:
            head=list1
            if list1.next==None:
                head.next=list2
                return head
            else:
                list1=list1.next
        else:
            head=list2
            if list2.next==None:
                head.next=list1
                return head
            else:
                list2=list2.next

        current=head
        while list1 and list2:
            if list1.val<=list2.val:
                next_temp=list1
                list1=list1.next
                current.next=next_temp
                current=next_temp
                if list1==None:
                    current.next=list2
                    return head
            else:
                next_temp=list2
                list2=list2.next
                current.next=next_temp
                current=next_temp
                if list2==None:
                    current.next=list1
                    return head

    def mergeTwoLists_2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        dummy + tail 模板写法

        时间复杂度：O(m+n)
        空间复杂度：O(1)
        """
        # dummy 是虚拟头结点，统一处理头节点逻辑
        dummy = ListNode()
        # tail 始终指向已合并链表的最后一个节点
        tail = dummy

        # 两条链表都还有节点时，挑更小的接到 tail 后面
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # 尾指针后移，保持 tail 永远在末尾
            tail = tail.next

        # 把未耗尽的一条链表直接接到末尾
        tail.next = list1 if list1 else list2

        # 返回真实头节点（跳过 dummy）
        return dummy.next
