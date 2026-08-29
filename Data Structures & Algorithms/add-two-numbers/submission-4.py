# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        quotient = 0

        while l1 or l2 or quotient:
            if l1 and l2:
                summ = (l1.val + l2.val)
            elif l1:
                summ = l1.val
            elif l2:
                summ = l2.val
            else:
                summ = 0
            
            remainder = (summ + quotient) % 10
            quotient = (summ + quotient) // 10

            curr.next = ListNode(remainder)
            curr = curr.next
            
            if l1 and l2:                  
                l1 = l1.next
                l2 = l2.next
            elif l1:
                l1 = l1.next
            elif l2:
                l2 = l2.next
                

        return dummy.next        