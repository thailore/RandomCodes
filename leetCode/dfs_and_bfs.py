def dfs(nodeStart):
    stack = []
    seen = {}
    stack.append(start)

    while len(stack) > 0:
        currentNode = stack.pop()

        if currentNode not in seen:
            seen.update({currentNode: True})
            print currentNode

        for node in currentNode.neighbors: #or left, right etc just add all children to stack
            if node not in seen:
                stack.append(node)

from collections import deque
def bfs
    queue = deque()
    seen = {}
    while len(queue) > 0:
        currentNode = queue.pop()
    if currentNode not in seen:
        seen.update({currentNode: True})
        print(currentNode)
    for node in currentNode.children:
        if node not in seen:
            queue.appendleft(node)

