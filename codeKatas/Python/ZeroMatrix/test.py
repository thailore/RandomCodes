#!/usr/bin/env python

import unittest

from main import *

class ZeroMatrix(unittest.TestCase):

    def test_2x2(self):   
        self.assertEqual(zeroMatrix([[1,0],[3,4]]), [[0,0],[3, 0]])
    
    def test_3x3(self):   
        self.assertEqual(zeroMatrix([[1,0,3],[4,5,6],[7,8,9]]), [[0,0,0],[4,0,6],[7,0,9]])

if __name__ == '__main__':
    unittest.main()
