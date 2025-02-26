# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        if not head:
            return 0

        cur = head
        res = []

        while cur:
            res.append(cur.val)
            cur = cur.next

        res_rev = res[::-1]

        ans = 0

        for i in range(0, len(res_rev)):

            if res_rev[i] == 0:
                continue
            ans += 2 ** i
        return ans