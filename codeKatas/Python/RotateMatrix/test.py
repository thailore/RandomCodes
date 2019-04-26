#!/usr/bin/env python

import unittest

from main import *

class RotateMatrix(unittest.TestCase):

    def test_2x2(self):   
        self.assertEqual(rotateMatrix([[1,2],[3,4]]), [[3,1],[4, 2]])
    
    def test_3x3(self):   
        self.assertEqual(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]), [[7,4,1],[8,5,2],[9,6,3]])
    
    def test_4x4(self):   
        self.assertEqual(rotateMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]), [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]])

if __name__ == '__main__':
    unittest.main()
