class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        '''
        Understand
        Returning how many times the ant crosses the boundary.
        Must return int.
        Must have some sort of list; otherwise, reprompt user for input.
        
        Match
        Working with arrays and lists.
        
        Plan
        Create a variable that acts as the boundary.
        If boundary is crossed, count 1 time.
        
        Implement
        '''
        
        
        boundary_crossed = 0
        count = 0
       
        for i in nums:
            boundary_crossed += i
            
            if boundary_crossed == 0:
                count += 1
                
        return count
        
                
            
        # print(count)
        '''
        # Review
        
        # Evaluate
        
        '''