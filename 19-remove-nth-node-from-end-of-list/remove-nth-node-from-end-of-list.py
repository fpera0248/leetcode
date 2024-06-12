# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # U
        # remove nth node from end of list

        # M
        # linkedlist, multiple pass

        # P
        # iterate through linkedlist, add values to new list, reversed list, create new linkedlist with reversed values, remove values from node, reverse list again, return new list

        #I

     # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
   # U
        # remove nth node from end of list

        # M
        # linkedlist, multiple pass

        # P
        # iterate through linkedlist, add values to new list, reversed list, create new linkedlist with reversed values, remove values from node, reverse list again, return new list

        # I

        lst = []
        current = head

        # Traverse the linked list and append node values to the list
        while current:
            lst.append(current.val)
            current = current.next

        # Remove the nth element from the end of the list
        reversed_lst = lst[::-1]
        reversed_lst.pop(n - 1)
        original_lst = reversed_lst[::-1]

        # Create a dummy node to handle the case of removing the head node
        dummy = ListNode(0)
        curr = dummy

        # Create a new linked list from the modified list
        for val in original_lst:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
