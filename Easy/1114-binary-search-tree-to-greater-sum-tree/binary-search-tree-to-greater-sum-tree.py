# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = 0

        def dfs(node):
            nonlocal s
            if node is None:
                return
            dfs(node.right)      # Visit right subtree first (larger values)
            s += node.val        # Add current value to running sum
            node.val = s         # Update node with accumulated sum
            dfs(node.left)       # Visit left subtree last (smaller values)

        dfs(root)
        return root              # ✅ Return the transformed tree