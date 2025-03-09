from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        # Build an array 'alt' where alt[i] = 1 if the tile at i and the tile at (i+1) mod n are different, else 0.
        alt = [1 if colors[i] != colors[(i+1) % n] else 0 for i in range(n)]
        
        # For a group of k tiles, we need the (k-1) adjacent differences to all be 1.
        # Because the tiles form a circle, extend alt by the first (k-1) elements.
        extended_alt = alt + alt[:k-1]
        
        # Build prefix sums for the extended_alt array.
        ps = [0]
        for num in extended_alt:
            ps.append(ps[-1] + num)
        
        count = 0
        # For each possible starting index i in the circle, the sum of alt values in the window from i to i+k-2
        # is given by ps[i+k-1] - ps[i]. If this sum equals k-1, the group is alternating.
        for i in range(n):
            if ps[i + k - 1] - ps[i] == k - 1:
                count += 1
        
        return count