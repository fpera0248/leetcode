class Solution:
    def generateTheString(self, n: int) -> str:
        # If n is odd, return a string composed entirely of one letter (e.g., 'a').
        if n % 2 == 1:
            return 'a' * n
        # If n is even, return a string where one letter appears (n-1) times (an odd number)
        # and a different letter appears once.
        return 'a' * (n - 1) + 'b'