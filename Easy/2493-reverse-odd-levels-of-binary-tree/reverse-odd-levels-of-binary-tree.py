# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        '''
        sub function

        when node.right level changed
        when node left level change

        track each change with different variables and if level change is equal, swap those values

        if level not odd, discard values
        left = right
        call function
        return root
        '''

        def reverse(node_left, node_right, level):
            # Stop if either node is None
            if not node_left or not node_right:
                return

            # If both levels are equal and odd, swap their values
            if level % 2 == 1:
                node_left.val, node_right.val = node_right.val, node_left.val

            # Go deeper in mirrored fashion
            reverse(node_left.left, node_right.right, level + 1)
            reverse(node_left.right, node_right.left, level + 1)

        # Start recursion with level 1 from root’s two children
        reverse(root.left, root.right, 1)
        return root