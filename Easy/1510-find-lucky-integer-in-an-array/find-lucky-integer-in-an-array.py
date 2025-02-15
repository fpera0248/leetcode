class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}

        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        largest_lucky = -1

        for key, value in hashmap.items():
            if key == value:
                largest_lucky = max(largest_lucky, key)

        return largest_lucky