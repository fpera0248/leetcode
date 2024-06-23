# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        n = amount of versions 1indexed
        find FIRST bad version (binary search)

        M:
        binary search

        P:
        binary search on this list, find first bad version by calling to the api
        divide list by half everytime with binary search, left pointer should equal the first bad version of list once it is halfed
        return l

        [1,2,3,4,5]
             m.l r
        '''

        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

        
