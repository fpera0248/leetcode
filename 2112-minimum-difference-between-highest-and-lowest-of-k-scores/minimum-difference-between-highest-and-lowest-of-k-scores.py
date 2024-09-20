class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        '''
        U:
        0 indexed ar, nums[i represents score of i th student]
        pick scores any any k student so that the differentce from highest to lowest is minimized
        return min possibel diff as int

        M:
        arr problem
        sort

        P:
        brtue force:
        iterate through list in two loops, find the k scores with the lowest difference (k makes this problem sliding window)
        sort(nlogn time)


        I:
        '''
        nums.sort(reverse=True)

        if len(nums) == 1:
            return 0

# Instead of subtracting values, find the difference between the largest and the k-th largest
        min_diff = float('inf')
        
        for i in range(len(nums) - k + 1):
            min_diff = min(min_diff, nums[i] - nums[i + k - 1])

        return min_diff

        '''

        R:

        E:


        '''  