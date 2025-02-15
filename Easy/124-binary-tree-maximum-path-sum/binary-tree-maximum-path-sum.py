from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')  # Step 1: Initialize to negative infinity

        def maxSum(node):
            if not node:  # Step 2: Base case
                return 0

            # Step 3: Compute left and right max path contributions (ignore negatives)
            left = max(0, maxSum(node.left))  
            right = max(0, maxSum(node.right))

            # Step 4: Update self.res with the max path sum including current node
            self.res = max(self.res, left + right + node.val)

            # Step 5: Return the max single-path contribution to the parent
            return node.val + max(left, right)

        maxSum(root)  # Start recursion from the root
        return self.res  # Return the maximum path sum