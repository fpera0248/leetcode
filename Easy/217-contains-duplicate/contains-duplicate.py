class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        #UMPIRE

        Understand
        nums = [1,2,3,1] -> True

        nums = [1,2,3,4] -> False

        if empty return True

        Match:
        dicitonary or list problem

        Plan
        # create dicitonary to count the amount of occurrences of each value, if value occurs more than once return true else false

        Implement
        '''

        dup = {}

        if not nums:
            return True

        for value in nums:
            if value in dup:
                dup[value] += 1
            else:
                dup[value] = 1

        for i in dup.values():
            if i >= 2:
                return True
        return False