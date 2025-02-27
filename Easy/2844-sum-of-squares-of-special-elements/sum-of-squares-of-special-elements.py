class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0, len(nums)):
            if len(nums) % (i + 1) == 0:                
                print(nums[i])
                ans += (nums[i]*nums[i])

        return ans