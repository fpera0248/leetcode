class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''

        U:
        Find intersection between both arrays, and the output must match the highest number of occurrences that happen in both arrays

        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2,2]

        M:
        intersection problem (could use sets)

        P:
        use set to find the intersection of both arrays, then utilize a for loop to search for the occurences of these intersection values in the arrays, and output a array with these values matching the occurences

        I:
        '''

        hashmap_nums1 = {}
        hashmap_nums2 = {}

        for i in nums1:
            hashmap_nums1[i] = hashmap_nums1.get(i, 0) + 1


        for i in nums2:
            hashmap_nums2[i] = hashmap_nums2.get(i, 0) + 1

        commonKeys = hashmap_nums1.keys() & hashmap_nums2.keys()

        print(commonKeys)

        res = []

        for key in commonKeys:
            min_count = min(hashmap_nums1[key], hashmap_nums2[key])
            res.extend([key] * min_count)

        return res

