class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
        res = 0

        for i in range(len(words)):
            for j in range(1, len(words)):
                if words[i] == words[j][::-1] and 0 <= i < j < len(words):
                   
                    res += 1

        return res