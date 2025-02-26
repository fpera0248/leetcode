class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return -1

        if len(nums) == 2:
            return -1 
            
        nums.remove(min(nums))
        nums.remove(max(nums))


        if not nums:
            return -1
            
        return nums[0]