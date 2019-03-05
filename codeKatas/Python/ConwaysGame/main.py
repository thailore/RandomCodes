class ConwaysGame(object):

    def __init__(self):
        return None

    def createWorld(self, width, height):
        self.world = World(width, height)
        

class World(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.createGrid(width, height)
    
    def createGrid(self, width, height):
        grid = []
        for times in range(height):
            grid.append([])
            for nums in range(width):
                grid[times].append(0)
        return grid

    def getHealth(self, x, y):
        return True if self.grid[x][y] == 1 else False 

    def setHealth(self, x, y, value):
        self.grid[x][y] = value

    def getNeighborsHealth(self, )
