class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        for key, value in enumerate(nums):
            hashmap[key] = value
        
        res = 0
        
        # Iterate over a copy of the dictionary items to avoid modifying while iterating.
        for key, value in list(hashmap.items()):
            if value < k:
                del hashmap[key]
                res += 1
        return res