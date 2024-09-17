class Solution:
    def greatestLetter(self, s: str) -> str:
        

        hashmap = {}

        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        res = []

        for key, value in hashmap.items():
            if key.upper() in hashmap and key.lower() in hashmap:
                res.append(key.upper())

        if res:
            return max(res)
        else:
            return ''
