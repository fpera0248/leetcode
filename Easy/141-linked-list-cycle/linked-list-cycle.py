# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ''' 
        store list node objects in an array
        if we encoutner the same list node object again, return true
        set iteration limit of twice the length of the list to avoid infinte loop

        '''

        arr = []
        cur = head

        while cur:

            if cur in arr:
                return True

            arr.append(cur)
            cur = cur.next
        return False


