class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        '''
        make list into a set to remove dups, check if list is longer than 3 items after making into set, find max, remove max from list, search for max again, until found the 3rd max
        '''

        nums_set = set(nums)

        if len(nums_set) < 3:

            return max(nums_set)
        
        for _ in range(2):
            top_value = max(nums_set)
            nums_set.remove(top_value)

        return max(nums_set)
