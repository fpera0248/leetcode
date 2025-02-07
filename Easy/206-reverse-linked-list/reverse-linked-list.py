# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        arr = []

        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next

        new_arr = arr[::-1]

        new_head = ListNode(new_arr[0])
        cur = new_head
        
        for i in range(1, len(new_arr)):
            cur.next = ListNode(new_arr[i])  # Create and link a new node
            cur = cur.next  # Move pointer forward
        return new_head

                            