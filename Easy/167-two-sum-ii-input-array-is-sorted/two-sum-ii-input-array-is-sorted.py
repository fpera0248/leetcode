class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        p1, p2 = 0, len(numbers) - 1

        if len(numbers) == 2:
            return [1, 2]

        while p1 < p2:
            current_sum = numbers[p1] + numbers[p2]

            if current_sum == target:
                return [p1 + 1, p2 + 1]

            elif current_sum > target:
                p2 -= 1
            else:
                p1 += 1