# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def univalued(node):
            if not node:
                return True

            return (node.val == root.val) and univalued(node.right) and univalued(node.left)

        return univalued(root)

