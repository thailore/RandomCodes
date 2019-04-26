#!/usr/bin/env python

import unittest

from main import *

class TestDuplicateInt(unittest.TestCase):

    def test_1234(self):   
        self.assertEqual(findBiggestNumWithDupInts(1234), 12344)
    
    def test_4321(self):   
        self.assertEqual(findBiggestNumWithDupInts(4321), 44321)
    
    def test_88989(self):   
        self.assertEqual(findBiggestNumWithDupInts(88989), 889989)

if __name__ == '__main__':
    unittest.main()
