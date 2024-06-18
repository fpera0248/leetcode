# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        length = 0
        count = 1
        
        while current:
            length += 1
            
            current = current.next
        
        current = head
        length = (length // 2) + 1
        
        while current:
            if count == length:
                print(current.val)
                return current
                
            count += 1
            current = current.next
