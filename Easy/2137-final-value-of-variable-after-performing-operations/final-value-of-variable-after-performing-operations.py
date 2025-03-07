class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0

        hashmap = {
         '++X' : 1,
         'X++' : 1,
         '--X' : -1,
         'X--' : -1
        }

        for i in operations:
            print(res)
            res += hashmap[i]
        return res

