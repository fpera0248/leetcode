class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        hashmap = {}

        for key, value in enumerate(nums):

            if value == target:
                return key
        return -1
        