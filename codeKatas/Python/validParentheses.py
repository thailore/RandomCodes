"""
Originally written on leetcode. Result was 12.8MB of memory (better than 100%) and 24ms (faster than 90%)
"""

def isValid(self, string: str) -> bool:
    pairs = {'(':')', '[':']', '{':'}'}
    stack = []

    for char in string:
        if char in pairs.keys():
            stack.append(char)
        elif len(stack) > 0 and pairs.get(stack[-1]) == char:
            stack.pop()
        else: 
            return False

    return len(stack) == 0
