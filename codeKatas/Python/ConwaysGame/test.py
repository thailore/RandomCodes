import unittest
from main import *

class TestConwaysGame(unittest.TestCase):

    def setUp(self):
	    self.conway = ConwaysGame()

    def test_createWorld_sets_width_height(self):
        self.conway.createWorld(5, 10)
        self.assertEqual(self.conway.world.width, 5)
        self.assertEqual(self.conway.world.height, 10)

    def test_createWorld_generates_grid(self):
        self.conway.createWorld(3, 3)
        self.assertIsNotNone(self.conway.world.grid)
    
    def test_getHealth_returns_value(self):
        self.conway.createWorld(3, 3)
        self.assertEqual(self.conway.world.getHealth(0,0), False) 
        self.assertEqual(self.conway.world.getHealth(1,1), False) 
        self.assertNotEqual(self.conway.world.getHealth(2,2), True) 

    def test_setCoordinateHealth(self):
        self.conway.createWorld(3,3)
        self.conway.world.setHealth(1, 1, 1)
        self.assertEqual(self.conway.world.getHealth(1,1), True)
        self.conway.world.setHealth(1, 1, 0)
        self.assertEqual(self.conway.world.getHealth(1,1), False)
        self.conway.world.setHealth(1, 2, 1)
        self.assertEqual(self.conway.world.getHealth(1,2), True)
        
    def test_getNeighborsHealth_returns_values(self):
        self.conway.createWorld(3,3)
        self.assertEqual(self.conway.world.getNeighborsHealth(0,0), 1)
        self.assertEqual(self.conway.world.getNeighborsHealth(1,1), 0)
        


if __name__ == '__main__':
    unittest.main()
