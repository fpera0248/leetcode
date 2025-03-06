class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        seen = set()
        duplicates = set()
        for num in nums:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        return list(duplicates)