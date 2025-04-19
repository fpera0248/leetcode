class Solution:
    def alternateDigitSum(self, n: int) -> int:

        digits = list(map(int, str(n)))  # Keep original order

        res = 0
        
        for i in range(len(digits)):
            res += digits[i] * (-1 if i % 2 else 1)  # alternate sign starting with +
        return res
