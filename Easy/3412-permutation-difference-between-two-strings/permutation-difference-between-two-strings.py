class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hash_s, hash_t = {}, {}

        # Map each character in s to its index.
        for index, char in enumerate(s):
            hash_s[char] = index

        # Map each character in t to its index.
        for index, char in enumerate(t):
            hash_t[char] = index

        res = 0

        # For each character in s, add the absolute difference 
        # between its index in s and its index in t.
        for char in hash_s:
            res += abs(hash_s[char] - hash_t[char])
            
        return res