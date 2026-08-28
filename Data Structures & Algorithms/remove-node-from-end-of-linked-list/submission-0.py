# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        dummy = ListNode(next=prev)
        curr2 = prev
        prev2 = dummy
        i = 0
        while curr2:
            i += 1
            nxt = curr2.next

            if i == n:
                prev2.next = nxt
            else:
                prev2 = curr2

            curr2 = nxt


        prev = None
        curr2 = dummy.next

        while curr2:
            nxt = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = nxt

        return prev