# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(n) run time, where n is the amount of tree nodes

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        
        return max(leftMax, rightMax) + 1
