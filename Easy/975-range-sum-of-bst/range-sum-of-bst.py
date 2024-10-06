# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        def rangeSum(root):
            nonlocal res  # To modify the outer `res` variable

            if not root:
                return  # Base case: if the node is None, return nothing

            # Traverse the left subtree first
            rangeSum(root.left)

            # Check the current node value
            if low <= root.val <= high:
                res += root.val

            # Traverse the right subtree
            rangeSum(root.right)

        # Call the helper function with the root node
        rangeSum(root)

        return res