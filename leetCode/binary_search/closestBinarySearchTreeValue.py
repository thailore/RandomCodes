# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286
"""


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        
        while root:
            closest = min(root.val, closest, key=lambda x: abs(x-target))
            root = root.left if root.val > target else root.right
        return closest
