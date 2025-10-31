class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        res = []
        seen = []

        for i in nums:
            if i in seen:
                res.append(i)
            else:
                seen.append(i)
        return res