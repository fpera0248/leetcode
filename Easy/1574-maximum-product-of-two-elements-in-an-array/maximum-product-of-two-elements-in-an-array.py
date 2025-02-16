class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        traverse list
        track max in variable
        return value value at the end

        '''

        res = 0
        maximum = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                res = (nums[i] - 1) * (nums[j] - 1)

                if res > maximum:
                    maximum = res
        return maximum