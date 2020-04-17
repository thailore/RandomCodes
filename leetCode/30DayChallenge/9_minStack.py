"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []


    def push(self, x: int) -> None:
        if self.min == None or x < self.min:
            self.min = x
        self.stack.append(x)


    def pop(self) -> None:
        self.stack.pop()
        if self.min not in self.stack:
            if len(self.stack) == 0:
                self.min = None
            else:
                self.min = sorted(self.stack)[0]

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

