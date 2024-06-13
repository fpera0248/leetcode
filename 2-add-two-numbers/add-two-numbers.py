# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0
        count = 0

        while l1:
            value = l1.val * (10 ** count)
            sum1 += value
            count += 1
            l1 = l1.next
        
        count = 0
        while l2:
            value2 = l2.val * (10 ** count)
            sum2 += value2
            count += 1
            l2 = l2.next
        

        sum_total = sum1 + sum2
        sum_total = str(sum_total)
        
        dummy = ListNode()
        curr = dummy

        # Iterate over the digits of sum_total and create the linked list
        for digit in reversed(sum_total):
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next