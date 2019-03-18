#!/usr/bin/env python

import unittest

from main import *

class TestKata(unittest.TestCase):

    def test_4_Pairs(self):   
        self.assertEqual(numberOfPairsWithDifferenceK([1,7,5,9,2,12,3], 2), 4)
    
    def test_3_Pairs(self):   
        self.assertEqual(numberOfPairsWithDifferenceK([1,4,5,9,7,14,10], 3), 3)
    
    def test_0_Pairs(self):   
        self.assertEqual(numberOfPairsWithDifferenceK([1,7,5,9,2,12,3], 20), 0)

if __name__ == '__main__':
    unittest.main()
