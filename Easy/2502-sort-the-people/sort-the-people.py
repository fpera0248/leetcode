class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        
        h = heights.copy()  # Save original heights
        
        heights.sort(reverse=True)
        
        for i in range(len(heights)):
            if heights[i] != h[i]:
                # Find where this height was originally
                original_index = h.index(heights[i])
                res.append(names[original_index])
            else:
                res.append(names[i])
        
        return res