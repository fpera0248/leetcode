class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        res = 0

        for i in range(0, len(nums)):
            for j in range(1, len(nums)):

                if nums[i] + nums[j] < target and i < j:
                    res += 1

        return res
