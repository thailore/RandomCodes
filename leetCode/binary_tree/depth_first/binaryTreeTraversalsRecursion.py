# When traversing a Binary Tree recurisvely you essentially do the same thing every time, just in different order:
# the code will look something like:

def traverse(root):
	answer = []
	traverseRecursive(root, answer)
	return answer

def traverseRecursive(root, answer):
	if (root is None):
		return

	# preOrder Traversal
	answer.append(root.val) # root
	traverseRecursive(root.left) # left subtree
	traverseRecursive(root.right) # right subtree

	# inOrder Traversal
	traverseRecursive(root.left) # left subtree
	answer.append(root.val) # root
	traverseRecursive(root.right) # right subtree

	# postOrder Traversal
	traverseRecursive(root.left) # left subtree
	traverseRecursive(root.right) # right subtree
	answer.append(root.val) # root

# generally recursive traversals are a bit better and only have a runtime of O(n) and a space complexity of O(n)
# but in the case that the depth of the tree is too large, you can run into a stack overflow problem from all of the 
# levels in memory, which is where an iterative solution can come into play
