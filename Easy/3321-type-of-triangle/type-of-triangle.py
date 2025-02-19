class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Must have exactly three sides to form a triangle.
        if not nums or len(nums) != 3:
            return 'none'
        
        # Sort the sides so we can check the triangle inequality.
        a, b, c = sorted(nums)
        if a + b <= c:
            return 'none'
        
        # Use set logic to determine triangle type.
        distinct = len(set(nums))
        if distinct == 1:
            return 'equilateral'
        elif distinct == 2:
            return 'isosceles'
        elif distinct == 3:
            return 'scalene'