# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        levels = []
        self.addToLevels(root, 0, levels)
        return levels
    
    def addToLevels(self, root: TreeNode, level: int, levels: List[List[int]]):
        if level == len(levels):
            levels.append([])
        levels[level].append(root.val)
        if root.left is not None:
            self.addToLevels(root.left, level + 1, levels)
        if root.right is not None:
            self.addToLevels(root.right, level + 1, levels)
