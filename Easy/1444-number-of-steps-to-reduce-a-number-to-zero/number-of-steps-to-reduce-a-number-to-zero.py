class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            if num % 2 == 0:
                num //= 2  # Use integer division to keep num as an integer
            else:
                num -= 1
            steps += 1
        return steps