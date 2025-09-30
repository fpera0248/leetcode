class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        nums.sort()
        res = []
        n = True
        k = 3
        total = sum(nums[0:3])  # Calculate initial sum once

        while n == True:
            largest = nums[k-1]
            
            if total - largest > largest:
                res.append(total)
            
            k += 1

            if k > len(nums):
                n = False
            else:
                total += nums[k-1]  # Add next element to running sum

        return max(res) if res else -1