# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        U:
        given an array of k linked lists
        combine and merge all linked list and sort

        if empty return None

        M:
        linked list/array traversal

        P:
        for index in lists:
            for number in index:
        
        add everythign to an array
        then sort array logn
        then create a linked list and return the head

        I:
        '''

        if not lists:
            return None

        arr = []

        for head in lists:
            current = head
            
            while current:
                arr.append(current.val)
                current = current.next

        if not arr:  # Ensure arr is not empty before accessing elements
            return None

        new_arr = sorted(arr)
        
        head = ListNode(new_arr[0])
        cur = head

        for i in range(1, len(new_arr)):
            cur.next = ListNode(new_arr[i])
            cur = cur.next
        return head
        

        

        