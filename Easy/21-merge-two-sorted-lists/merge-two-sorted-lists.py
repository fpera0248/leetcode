# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        U:
        given two already sorted lists
        merge both into one sorted list and return head

        M:

        linkedlist iteration problem
        two pointer

        P:
        brute force:
        turn both list into arrays, sort them then re-create the list 0(n)
        if both empty return None

        I

        '''

        if not list1 and not list2:
            return None

        arr = []
        cur1 = list1
        cur2 = list2

        while cur1:
            arr.append(cur1.val)
            cur1 = cur1.next

        while cur2:
            arr.append(cur2.val)
            cur2 = cur2.next

        new_arr = sorted(arr)

        new_head = ListNode(new_arr[0])

        cur = new_head

        for i in range(1, len(new_arr)):
            cur.next = ListNode(new_arr[i])
            cur = cur.next
        return new_head
