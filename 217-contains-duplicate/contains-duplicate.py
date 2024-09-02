class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] = 1

        for key, value in hashmap.items():
            if value != 1:
                return True
        return False