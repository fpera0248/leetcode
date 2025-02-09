# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return []

        cur = head

        arr = []
        new_arr = []

        while cur:
            arr.append(cur.val)
            cur = cur.next

        if not arr:  # Ensure arr is not empty before accessing elements
            return None

        for i in range(0, len(arr), k):  # Iterate in steps of k
            if i + k > len(arr):  
                new_arr.extend(arr[i:])  # Append the remaining elements as they are
            else:
                new_arr.extend(arr[i:i+k][::-1])  # Reverse and append k-sized chunk



        head = ListNode(new_arr[0])
        cur = head

        for i in range(1, len(new_arr)):
            cur.next = ListNode(new_arr[i])
            cur = cur.next
        return head
        