class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []  # This will store the result counts
        
        # Loop over each element in nums
        for i in range(len(nums)):
            tracker = 0  # Reset tracker for each element
            
            # Compare the current element with every element in nums
            for j in range(len(nums)):
                # Ensure we don't compare the element with itself
                if j != i and nums[j] < nums[i]:
                    tracker += 1
            
            # Append the count of numbers smaller than nums[i]
            res.append(tracker)
        
        return res