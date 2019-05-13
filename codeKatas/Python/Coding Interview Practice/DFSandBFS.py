from collections import deque


def depth_first_search(node):
    if node == null:
        return
    print(node.value)
    depth_first_search(node.left())
    depth_first_search(node.right())
    # Preorder DFS


def breadth_first_search(startingNode, searchedValue):
    visitedNodes = set()
    queue = deque([startingNode])
    while len(queue) > 0:
        node = queue.pop()
        if node in visitedNodes:
            continue
        visitedNodes.add(node)
        
        if node.value == searchedValue:
            return True
        for n in node.neighbors:
            if n not in visitedNodes:
                queue.appendleft(n)
    return False
    
    
    
