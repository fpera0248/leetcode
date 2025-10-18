class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        # If n = 1, all 1-digit numbers are valid
        if n == 1:
            return [i for i in range(10)]

        result = []

        # Start DFS from digits 1–9 (no leading zeros)
        def dfs(num, length):
            if length == n:
                result.append(num)
                return

            last_digit = num % 10
            # Try adding +k and -k
            next_digits = set([last_digit + k, last_digit - k])

            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    dfs(num * 10 + next_digit, length + 1)

        for i in range(1, 10):
            dfs(i, 1)

        return result