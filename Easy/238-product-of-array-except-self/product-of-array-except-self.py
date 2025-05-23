class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        UMPIRE

        U:
        input array
        output array

        min arr length of 2

        product on entire list besides arr, algo needs 0(n) time complexity and no division

        M:
        arr traversal

        P:

        traverse through each elemnt in nums
        create replacement arr icnlduing all values except self
        add the product of these values to an element, and output this element to the answer arr
        '''

        from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # Calculate prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        # Calculate suffix products and multiply into output
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output
        