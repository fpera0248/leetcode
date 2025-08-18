# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        '''
        root, iterative 
        
            1
        2        3
        
    4       5   6
        
    root = [1,2,3,4,5,6]
        '''
        
        if not root:
            return 0
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        
        
        