class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        
        col1 = ord(coordinate1[0]) - ord('a') + 1
        col2 = ord(coordinate2[0]) - ord('a') + 1

        row1 = int(coordinate1[1])
        row2 = int(coordinate2[1])

        res1 = (col1 + row1)
        res2 = (col2 + row2)

        print(res1, res2)

        return (res1 % 2) == (res2 % 2)
            
