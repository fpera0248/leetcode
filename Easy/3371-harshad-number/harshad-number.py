class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        res = 0
        track = []

        for i in str(x):
            res += int(i)

        if x % res == 0:
            return res
        return -1