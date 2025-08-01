class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        value = 0
        final_arr = []
        
        for i in nums:
            value += i
            final_arr.append(value)
        return final_arr