class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        '''
        U:
        move all zeros to the end of the list by keeping the relative order of the array

        M:
        two pointers

        P:
        use two pointer to iterate throguh the list, if first element is 0, make copy of second number in temrp variable , and switch position
        Input: nums = [0,1,0,3,12]

        if 0 on left, move right
        if 0 on right, move left

        [1,0,0,3,12]
           l   r

        [4, 5, 9, 0 , 0 ,6 ,0 ,12 ,5]
                   l,        r


        [1,3,12,0,0]


        I:
        '''

        left, right = 0, 1

        while right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp 
            
                left += 1
                right += 1

            elif nums[left] == 0 and nums[right] == 0:
                right += 1
            
            else:
                # Move both pointers forward if the left element is not zero
                left += 1
                right += 1

     