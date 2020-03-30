# Traversals https://leetcode.com/articles/Figures/145_transverse.png

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        self.addToList(root, answer)
        return answer
    
    def addToList(self, root: TreeNode, answer: List[int]):
        if root is not None:
            if root.left is not None:
                self.addToList(root.left, answer)
            if root.right is not None:
                self.addToList(root.right, answer)
            answer.append(root.val)
            
            
    def iteratively():
        if root is None:
            return []
        
        stack, answer = [root], []
        
        while stack:
            root = stack.pop()
            answer.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        return answer[::-1]
