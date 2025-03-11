class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # Get the number of rows (m) and columns (n) in the matrix
        m = len(matrix)
        n = len(matrix[0])

        # Create a new matrix "ans" filled with zeros
        ans = [[0] * n for _ in range(m)]

        # Create a list "col" to store maximum elements in each column, initially filled with -1
        col = [-1] * n

        # Step 1: Iterate through each column of the matrix
        for i in range(n):
            # Step 2: Iterate through each row of the matrix
            for j in range(m):
                # Step 3: Copy elements from the original matrix to the "ans" matrix
                ans[j][i] = matrix[j][i]
                
                # Update the "col" list with the maximum element in the current column
                col[i] = max(col[i], matrix[j][i])

        # Step 4: Iterate through each element in the "ans" matrix
        for i in range(n):
            for j in range(m):
                # Step 5: If the element is -1, replace it with the maximum value from its column
                if ans[j][i] == -1:
                    ans[j][i] = col[i]

        # Return the modified "ans" matrix
        return ans