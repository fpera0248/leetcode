class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res = ''
        for i in range(len(words)):
            res += (words[i][0])
        return res == s