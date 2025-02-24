class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        # Saving all "1" bits
        for num in nums:
            result |= num
        # Finding the sum (equivalent to (2^(x - 1)) * 2^(n - 1) )
        return result << (len(nums) - 1)