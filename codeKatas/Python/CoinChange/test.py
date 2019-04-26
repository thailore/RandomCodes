#!/usr/bin/env python

import unittest

from main import *

class TestCoinChange(unittest.TestCase):

    def test_100(self):   
        self.assertEqual(getChange([25, 10, 5, 1], 100), 4)
    
    def test_103(self):   
        self.assertEqual(getChange([25, 10, 5, 1], 103), 7)
    
    def test_85(self):   
        self.assertEqual(getChange([25, 10, 5, 1], 85), 4)

if __name__ == '__main__':
    unittest.main()
