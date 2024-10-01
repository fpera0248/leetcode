# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        U:
        track longest path from root to farthest leaf
        including root node in total count

        bad case:
        empty tree - return 0


        M:
        binary tree traversal, dfs


        P:
        iterate through each level of the bianry tree, tracking the longest path 
                    3
                   / \
                  9  20 
                    /  \
                   15   7
                     \
                      6

        iterative approach: traverse through left side of tree, if leaf node(no children) move back up and review next node on left side, track the longest path
        do the same for right side

        recursive approach: create function for recursive tranversal, iterate through each side, find a way to collect and track teh longest path for leaf nodes  
        out put int of longest path
        
        I:
        '''
        if not root:
            return 0

        #iterative
      #  while root.left:
            


        count = 1
        res = []

        #recursive
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)


        # if root.left == None and root.right == None:
        #     res.append(count)
        #     count -= 1
        # else:
        #     count += 1


        # for i in self.maxDepth(root.right):
        #     if root.left == None and root.right == None:
        #         res.append(count)
        #         count -= 1
        #     else:
        #         count += 1

        return max(left, right) + 1



        '''    
        R:



        E:


        '''