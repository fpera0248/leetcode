class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        value = 0
        p1, p2 = 0, 1

        value += nums[p1]
        res.append(nums[p1])
        print(value)

        for _ in range(p2, len(nums)):
            value += nums[p2]
        
            res.append(value)
            
            p2 += 1
        return res