class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False  # cycle detected
            seen.add(n)

            # Compute the sum of the squares of digits
            n = sum(int(digit) ** 2 for digit in str(n))

        return True
