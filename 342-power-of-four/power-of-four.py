class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        '''
        U:
        find a number x such that n == 4^x


        M:
        Recursion


        P:
        Create a recursive function that find if there is a value x such that n == 4^x
        try if different values to the power of four == n
        return true if x is found, else false

        I:
        '''

        def helper(x):

            if n < 0:
                return False

            if n == 0:
                return False

            if 4 ** x == n:
                return True

            if 4 ** x > n:
                return False 

            return helper(x+1)

        return helper(0)
