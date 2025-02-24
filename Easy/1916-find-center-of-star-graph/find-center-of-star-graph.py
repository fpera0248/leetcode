class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Create an empty dictionary to count vertex occurrences
        dictionary = {}

        # Iterate over each edge and then over each vertex in the edge
        for edge in edges:
            for vertex in edge:
                if vertex in dictionary:
                    dictionary[vertex] += 1
                else:
                    dictionary[vertex] = 1

        # In a star graph, the center vertex appears in every edge.
        # Since there are len(edges) edges, the center's count should be equal to len(edges).
        for vertex, count in dictionary.items():
            if count == len(edges):
                return vertex

        # In a valid star graph, this point should never be reached.
        return -1