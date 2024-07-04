class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ''' 
        if interger n is a power of 2, meaning 2^x == n

        Recursive

        create a recusrive function call, if 2^x == n, return true else false
        x= 0, while x < n, base case x//2


        '''
        if n == 1:
            return True

        if n <= 0:
            return False

        def helper(x):
            if 2 ** x == n:
                return True
                
            # If 2^x exceeds n, return False
            elif 2 ** x > n:
                return False
                
            # Recursive case: increment x and check again
            return helper(x + 1)
        
        # Start recursion with x = 0
        return helper(0)
