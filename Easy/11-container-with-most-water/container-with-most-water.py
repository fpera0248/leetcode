class Solution:
    def maxArea(self, height: List[int]) -> int:
        #   min(heights[x],heights[y]) * (distance between x and y)
        
        '''
        index, value 
        
        enumerate list, 
        
        output max container where distance * lesser of two heights is grreatest
        
        
        '''
        container = 0
        p1, p2 = 0, len(height) - 1 
        
        # p1=0,p2=n-1
        while p1 < p2:
            # for i in range(len(height)):
                container = max(container, (min(height[p1], height[p2]) * (p2 - p1) ))
                
                if height[p1] < height[p2]:
                    p1 += 1
                else:
                    p2 -= 1
                    
        return container
            
            
            
            
        