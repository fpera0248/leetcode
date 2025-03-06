class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # Convert a coordinate to its color (True for white, False for black)
        def is_white(coordinate: str) -> bool:
            col = ord(coordinate[0]) - ord('a') + 1  # Convert 'a'-'h' to 1-8
            row = int(coordinate[1])
            return (col + row) % 2 == 0
        
        return is_white(coordinate1) == is_white(coordinate2)