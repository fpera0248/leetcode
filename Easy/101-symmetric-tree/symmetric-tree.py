# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # Initialize a stack with a tuple containing the left and right children of the root.
        stack = [(root.left, root.right)]
        
        while stack:
            t1, t2 = stack.pop()
            # If both nodes are None, continue with the next pair.
            if not t1 and not t2:
                continue
            # If one is None or the values don't match, tree isn't symmetric.
            if not t1 or not t2 or t1.val != t2.val:
                return False
            # Add the children pairs in the order that maintains the mirror comparison.
            stack.append((t1.left, t2.right))
            stack.append((t1.right, t2.left))
        
        return True