class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        '''

        fidn two largest nums, - two smallest numbers

        '''

        w = max(nums)
        nums.remove(w)

        x = max(nums)

        y = min(nums)
        nums.remove(y)

        z = min(nums)

        return (w*x) - (y*z)