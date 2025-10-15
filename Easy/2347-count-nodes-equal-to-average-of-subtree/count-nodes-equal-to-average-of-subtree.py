# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0  # tracks number of nodes satisfying the condition

        def subtree(node):
            nonlocal count
            if not node:
                return (0, 0)  # (sum, number of nodes)

            left_sum, left_count = subtree(node.left)
            right_sum, right_count = subtree(node.right)

            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            avg = total_sum // total_count  # rounded down automatically
            if node.val == avg:
                count += 1

            return (total_sum, total_count)

        subtree(root)
        return count