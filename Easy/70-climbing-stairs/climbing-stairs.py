class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        dp = [0] * n

        dp[0] = 1
        dp[1] = 2

        for steps in range(2, len(dp)):
            dp[steps] = dp[steps - 2] + dp[steps - 1]

        return dp[-1]