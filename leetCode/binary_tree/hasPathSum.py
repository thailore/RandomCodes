# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        currentSum = sum - root.val
        if root.left is None and root.right is None and currentSum == 0:
            return True
        
        return self.hasPathSum(root.left, currentSum) or self.hasPathSum(root.right, currentSum)    
        
