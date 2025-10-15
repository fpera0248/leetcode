# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        max_depth = 0
        total = 0

        def run(node, depth):
            nonlocal max_depth, total
            if not node:
                return

            # If it's a leaf node
            if not node.left and not node.right:
                if depth > max_depth:
                    max_depth = depth
                    total = node.val      # start new sum at new max depth
                elif depth == max_depth:
                    total += node.val     # add to current deepest sum
                return
            
            # Recurse left and right
            run(node.left, depth + 1)
            run(node.right, depth + 1)

        run(root, 0)
        return total