class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        print (set(nums))
        print (nums)

        if len(set(nums)) != len(nums):
            return True
        return False

        