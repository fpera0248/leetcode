class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        '''
        P:
        merge nums1 with nums2 : nums1[:m] = nums2
        then sort and return nums1
        '''

        nums1[m:] = nums2
        print(nums1)
        nums1 = nums1.sort()


        