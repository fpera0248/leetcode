# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # If the node is a leaf node
        if not root.left and not root.right:
            return 1
        
        # If left subtree is None, then consider the right subtree only
        if not root.left:
            return self.minDepth(root.right) + 1
        
        # If right subtree is None, then consider the left subtree only
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # If both left and right subtrees exist, consider the minimum of both
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        return min(left_depth, right_depth) + 1