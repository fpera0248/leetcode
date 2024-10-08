# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def pathSum(node, currentSum):
            # Base case: if we reached a leaf node, check if the current sum equals targetSum
            if not node.left and not node.right:
                return currentSum + node.val == targetSum

            # Initialize left and right results to False
            left = right = False

            # Recurse on the left child if it exists
            if node.left:
                left = pathSum(node.left, currentSum + node.val)
            
            # Recurse on the right child if it exists
            if node.right:
                right = pathSum(node.right, currentSum + node.val)

            # Return True if either left or right path satisfies the condition
            return left or right
        
        # Call the pathSum function starting from the root with an initial sum of 0
        return pathSum(root, 0)
            
            
