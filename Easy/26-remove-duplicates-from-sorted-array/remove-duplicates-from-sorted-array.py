class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        p1 = 0

        # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        #         p1 p2
        for p2 in range(1, len(nums)):
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]

        return p1 + 1