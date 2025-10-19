class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        

        '''
        arr pos int
        return distinct prime factors 


        1024




        '''
        distinct = set()
        
        for n in nums:
            d = 2
            # trial division
            while d * d <= n:
                if n % d == 0:
                    distinct.add(d)
                    while n % d == 0:
                        n //= d
                d += 1
            if n > 1:
                # whatever remains is prime
                distinct.add(n)
        
        return len(distinct)