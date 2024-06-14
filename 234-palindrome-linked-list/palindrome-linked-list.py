# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        iterate through list, add all values to a list, create new list of reversed values
        if both list are equal return true else false


        '''

        lst = []

        while head:
            lst.append(head.val)
            head = head.next

        reversed_lst = lst[::-1]

        if lst == reversed_lst:
            return True
        return False