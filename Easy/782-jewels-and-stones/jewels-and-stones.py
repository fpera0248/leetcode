class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        res = set(jewels)
        output = 0

        for i in stones:
            if i in res:
                output += 1
        return output
