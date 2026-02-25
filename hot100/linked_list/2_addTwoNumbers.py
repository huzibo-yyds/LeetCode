# 两数相加 两个非空链表倒序
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1,num2=0,0
        head1,head2=l1,l2
        place1, place2 = 1, 1
        while head1:
            num1 += head1.val * place1
            place1 *= 10
            head1=head1.next
        while head2:
            num2 += head2.val * place2
            place2 *= 10
            head2=head2.next
        sum = num1+num2

        if sum == 0:
            return ListNode(0)

        dummy=ListNode()
        tail=dummy

        while sum>0:
            temp=sum%10
            sum=sum//10
            temp_node=ListNode(temp)
            tail.next=temp_node
            tail=tail.next
        
        return dummy.next
