class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        res = 0

        for i in s:
            if i == letter:
                res += 1

        return int((res / len(s)) * 100)
