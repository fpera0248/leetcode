class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: 
            return False
        target = total // 2

        possible = {0}
        for x in nums:
            nxt = set()
            for s in possible:
                if s + x == target:
                    return True
                if s + x < target:
                    nxt.add(s + x)
            possible |= nxt
        return target in possible