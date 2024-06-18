# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr = []
  
        p1 = left - 1
        p2 = right - 1
        
        if not head:
            return []
            
        while head:
            arr.append(head.val)
            head = head.next
            
        p1 = left - 1
        p2 = right - 1
        
        while p1 <= p2:
            temp = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = temp
                    
            p1 += 1
            p2 -= 1
            
        newhead = ListNode(arr[0])
        current = newhead
        
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return newhead
