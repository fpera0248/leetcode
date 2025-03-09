from typing import List

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        res = []
        
        # Mountain 0 is not stable by definition, so start from index 1.
        for i in range(1, len(height)):
            # A mountain at index i is stable if the mountain immediately before it is strictly greater than threshold.
            if height[i-1] > threshold:
                res.append(i)
            print("Checking mountain at index", i, "with previous height", height[i-1], "->", res)
        
        return res