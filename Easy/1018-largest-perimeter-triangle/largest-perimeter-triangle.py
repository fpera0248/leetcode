


'''
int arr nums
return largest perimeter of trinagle with a non zero area


a+b > c, if a + b = c triangle collapes


sort with largest value in front 

maximum actual perimeter
have to track output and maximum value in array

if nums size three, check a + b > c

10 2 1 1
i  j c
1 1 2 10


'''

from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()  # sort ascending
        n = len(nums)

        # check triples from largest to smallest
        for i in range(n - 1, 1, -1):
            a, b, c = nums[i-2], nums[i-1], nums[i]
            if a + b > c:
                return a + b + c
        return 0