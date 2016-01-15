class Node:
    def _init_(self, value):
        self.value = value
        self.left = []
        self.right = []

    def add_child(self, value):
        n = Node(value)
        if n.value < self.value:
            self.add_left(n)
        else:
            self.add_right(n)
            


    def add_left(self, value)


