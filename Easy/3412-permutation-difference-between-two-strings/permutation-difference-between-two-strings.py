class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        hash_s, hash_t = {}, {}

        for index, value in enumerate(s):
            hash_s[value] = index

        for index, value in enumerate(t):
            hash_t[value] = index

        res = 0

        for index, value in hash_s.items():
            if value in hash_t.values():
                res += abs(hash_s[index] - hash_t[index])

        return res

        
