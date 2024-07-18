# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
            
        def dfs(node):
            if not node:
                # Balanced, height
                return [True, 0]

            left = dfs(node.left) # balace, height
            if left[0] == False:
                return [False, None]
            right = dfs(node.right)
            if right[0] == False:
                return [False, None]
            # Height + 1 (don't need for the abs value formula bc we return that stuff)
            height = 1 + max(left[1], right[1])
            # condition
            balanced = (abs(left[1] - right[1])) <= 1
            return [balanced, height]
            

        val = dfs(root)
        return val[0]