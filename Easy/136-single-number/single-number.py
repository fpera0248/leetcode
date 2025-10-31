class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        counts = Counter(nums)
        for num, count in counts.items():
            if count == 1:
                return num