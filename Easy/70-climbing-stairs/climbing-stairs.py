class Solution:
    def climbStairs(self, n: int) -> int:
        '''

        dynamic programing

        U:
        n: int
        return int

        you can move forward either 1 or 2 steps

        return the distinct ways to climb to the top of the staircase(dp)

        M:

        dp - use tabulation (array) to track the increasing value of the ans
        ans return last value in arr 

        P:

        set the  two base cases, then iterate and create the new soltuions from there

        I:
        '''

        if n == 1:
            return 1

        if n == 2:
            return 2

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n-1]
