# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #while root:
        # example 2
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # example 1
        #elif root.val > p.val and root.val < q.val:
        #    return root #??? 
        # edge case
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
        
        
        
        
        
        
        
        
        
        '''
        recursive 
        
        if a root, and descendants p and q, return 
        can be itself, if p and q arent both descendants of something else
        
        level order, bfs?
        
        
        order = {}
        
        def dfs(node):
            if not node:
                return
                
            if node.left:
                order[node.left] = node
                dfs(node.left)
            
            if node.right:
                order[node.right] = node
                dfs(node.right)
        dfs(root)
        
        return order
        '''
        