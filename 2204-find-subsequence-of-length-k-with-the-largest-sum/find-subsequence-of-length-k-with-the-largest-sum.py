class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        nums_sorted = sorted(nums)
        nums_sorted_reverse = nums_sorted[::-1]
        
        hashmap = {}
        for index, value in enumerate(nums_sorted_reverse[:k]):
            if value not in hashmap:
                hashmap[value] = []
            hashmap[value].append(index)
        
        res = []
        for index, value in enumerate(nums):
            if value in hashmap and hashmap[value]:
                res.append(value)
                hashmap[value].pop(0)
                if len(hashmap[value]) == 0:
                    del hashmap[value]
            if len(res) == k:
                break
        
        return res
