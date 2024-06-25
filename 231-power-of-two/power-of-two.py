class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        return if value is power of 2, meaning if square root of n equals 

        sqrtn = 4
        2^4 = 16


        '''
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

