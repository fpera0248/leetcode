from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]], mid: int) -> bool:
        n = len(nums)
        temp = nums[:]
        delta = [0] * (n + 1)

        for i in range(mid):
            l, r, v = queries[i]
            delta[l] -= v
            if r + 1 < n:
                delta[r + 1] += v

        curr_decrement = 0
        for i in range(n):
            curr_decrement += delta[i]
            temp[i] += curr_decrement
            if temp[i] > 0:
                return False
        return True

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left, right, ans = 0, len(queries), -1

        while left <= right:
            mid = (left + right) // 2
            if self.isZeroArray(nums, queries, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans