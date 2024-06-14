# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        U:
        Reverse linked list and return reversed list

        M:
        Linked list traversal, two pointers

        P:
        Reverse nodes of linkedlist from start, and to point to a dummy node
        keep track of current value so that link isnt lost
        continue this until everything is reversed

        for 1 -> 2 -> 3 -> 4 -> 5

        prev 1 -> 2 -> 3 -> 4 -> 5

        temp = current.next 

        prev <- 1 2 -> 3 -> 4 -> 5

        I:
        '''

        prev = None

        current = head

        while current:
            temp = current.next
            current.next = prev # prev <- 1  2 -> 3 -> 4 -> 5  
            prev = current
            current = temp
        return prev
