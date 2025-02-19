class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        
        for number in grid:
            for negative in number:
                if negative < 0:
                    res += 1
        return res