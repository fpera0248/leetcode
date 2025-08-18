# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Left Subtree: Root: Right Subtree: 
        
        1
            2
        3
        
        Output: [1,3,2]
        '''
        if root is None:
            return []
        
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        
        return left + [root.val] + right
        
        
        
        