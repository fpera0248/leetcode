from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # Return an empty list if the tree is empty

        res = []                   # Final result list
        queue = deque([root])      # Start the queue with the root node

        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level = []               # List to store the current level values

            for _ in range(level_size):
                node = queue.popleft()      # Dequeue a node
                level.append(node.val)      # Append its value to the level list

                # Add left child if it exists
                if node.left:
                    queue.append(node.left)
                # Add right child if it exists
                if node.right:
                    queue.append(node.right)

            res.append(level)  # Append the level list to the result

        return res