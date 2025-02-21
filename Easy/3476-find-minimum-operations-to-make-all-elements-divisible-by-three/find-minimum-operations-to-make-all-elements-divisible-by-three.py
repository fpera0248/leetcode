class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        '''
        U:
        int array = nums

        return int

        nums: [10,11,12,13]
        4

        []
        return 0

        [-1, -9, 0, 3]


        M:
        array traversal: iterate through nums, if modulo 3 == 0, 
        track the amount of steps in a variable
        if modulo 3 == 1, subtract 1
        modulo 3 == 2: add 1
        else Print(value)

        time: 0(n)
        space: 0(n)

        P:
        '''
        res = 0

        for i in nums:
            if i % 3 == 1 or i % 3 == 2:
                res += 1
            else:
                continue
            
        return res      
