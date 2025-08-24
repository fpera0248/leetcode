

'''

strings jewels : stones that are jewels

stones: stones i have

each cahracter in tones is a tone you have

find how mnay stone are also jewels

plan:

use jewels to track how many times each index occurs in stones, and add counter for each time then return counter
'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        res = 0
        jewels_new = set(jewels)

        for i in stones:
            if i in jewels_new:
                res += 1
        return res

