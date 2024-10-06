class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        res = []
        count = 0

        for i in nums:

            if i == 1:
                count += 1
            
            else: 
                res.append(count)
                count = 0
                
        res.append(count)

        return max(res)

        