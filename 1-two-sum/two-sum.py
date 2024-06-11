class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        UMPIRE

        Understand:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]

        will not be empty, exactly one solution

        Match:
        dicitnoary porblem

        Plan:

        create dicitonary, use enaumrate to create a key, value pair in dicitnary form with key being the value
        check if their is a value that complements the values, subtracts it and sees if their is a value that reaches target in the dicitonary, return the indice values

        Implement
        '''
        twoSum = {}

        for key, value in enumerate(nums):
           if target - value in twoSum:
                return [key, twoSum[target-value]] # Return the indices
           twoSum[value] = key

    '''
    Review: 
    '''