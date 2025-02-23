class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Initialize tracker list with the first two edges
        tracker = [edges[0], edges[1]]
        res = 0

        # Iterate through each edge starting from index 1
        for i in range(1, len(edges)):
            # For each vertex in the current edge
            for vertex in edges[i]:
                # Check if the vertex exists in both tracker edges
                if vertex in tracker[0] and vertex in tracker[1]:
                    res = vertex
        return res