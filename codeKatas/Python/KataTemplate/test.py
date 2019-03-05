import unittest

from main import *

class TestKata(unittest.TestCase):

    def setUp(self):
	    self.kata = Kata()

    def test_upper(self):   
        self.assertEqual(self.kata.test(), True)

if __name__ == '__main__':
    unittest.main()
