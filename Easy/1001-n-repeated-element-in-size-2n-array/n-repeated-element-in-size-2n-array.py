class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        for key, count in hashmap.items():
            if count > 1:
                return key