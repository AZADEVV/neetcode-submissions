# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        before_left = dummy
        left_node = head
        right_node = head

        count = right - left + 1

        for _ in range(left - 1):
            before_left = before_left.next

        left_node = before_left.next

        right_node = left_node
        for _ in range(count - 1):
            right_node = right_node.next

        prev = right_node.next
        curr = left_node

        while count > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count -= 1

        before_left.next = prev

        return dummy.next



