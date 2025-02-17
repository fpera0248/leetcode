class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        nums: int arr (increasing order)
        return: arr of square of each number in increasing order

        if empty return 0



        '''

        res = []

        for i in nums:
            res.append(i*i)
        
        return sorted(res)