# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:

            if current.val == current.next.val:  # if the current val and next val are equal (dup)
                current.next = current.next.next   # Point current.next to current.next.next

            else:
                current = current.next 

        return head
        