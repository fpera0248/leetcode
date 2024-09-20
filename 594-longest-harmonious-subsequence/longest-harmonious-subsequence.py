class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ''' 
        U:
        diff between max and min is exactly 1 = harmonius arr
        given an int arr, return the length of the longes subsequece

        subsequence = allows removal of elements, but keeps them in same order
        negatieve and positive values

        return type int

        arr = [2,3,4,9,5,4,6]
        output = 2,3,4,5,6 = 2

        worst case:
        if empty return 0

        1,5,7,0
        output = 2

        M:
        brute force: double for loop
        first loop stay at first indice, ,second loop iterate throguh rest of arr
        output arr to store length

        P:
        set up coutner variable, and add that vairable to ares array
        setup for loop to iterate through nums and the indices
        return the max of res arr


        I:
        '''

        counter = 0
        res = []

        if not nums:
            return 0

        # Count the frequency of each number
        num_count = Counter(nums)
        max_len = 0

        # Iterate through each unique number in the list
        for num in num_count:
            # Check if the next consecutive number exists
            if num + 1 in num_count:
                # Find the total length of the subsequence including num and num + 1
                max_len = max(max_len, num_count[num] + num_count[num + 1])

        return max_len

        # '''
        # R:
