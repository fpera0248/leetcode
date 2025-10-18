import math
from functools import lru_cache

class Solution:
    def soupServings(self, n: int) -> float:
        # Optimization: for large n, answer ~ 1
        if n > 4800:
            return 1.0

        n = math.ceil(n / 25)

        @lru_cache(None)
        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            return 0.25 * (
                dfs(a - 4, b) +
                dfs(a - 3, b - 1) +
                dfs(a - 2, b - 2) +
                dfs(a - 1, b - 3)
            )

        return dfs(n, n)