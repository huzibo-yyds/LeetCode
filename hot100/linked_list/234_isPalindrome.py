# 给但单链表头结点，判断是否回文链表

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    回文链表判断 - 快慢指针解法
    
    时间复杂度：O(n)，需要遍历链表三次（找中点、反转、比较）
    空间复杂度：O(1)，仅使用常数额外空间（指针）
    
    关键步骤：
    1. 快慢指针找链表中点
    2. 反转后半段链表
    3. 比较前半段和反转后的后半段
    '''
    # 翻转单链表
    def reverseList(self,head:Optional[ListNode])->Optional[ListNode]:
        '''原地反转链表，返回新头节点'''
        prev = None 
        current = head

        while current:
            next_temp = current.next  # 保存下一个节点
            current.next=prev  # 反转指针方向
            prev=current  # prev 向前移动
            current=next_temp  # current 向前移动
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''判断链表是否为回文，O(1)空间解法'''
        # 边界：空链表或单节点必为回文
        if head==None or head.next==None:
            return True
        
        # 快慢指针找中点：fast一次走两步，slow一次走一步
        # 循环结束后 slow 停在中点（奇数）或左边最后一个（偶数）
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 反转后半段链表（从slow开始）
        # 奇数时 slow 是中点，反转不包含中点
        # 偶数时 slow 是左半最后一个，反转包含右半第一个
        second = self.reverseList(slow)
        
        # 比较前半段和反转后的后半段
        # 由于反转后的后半段长度≤前半段，用 second 作循环条件自动处理奇偶
        first = head
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True

