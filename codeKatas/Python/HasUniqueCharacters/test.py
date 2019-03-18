#!/usr/bin/env python

import unittest

from main import *

class TestHasUniqueCharacters(unittest.TestCase):

    def test_unique_with_count(self):   
        self.assertEqual(isUniqueWithCount("abcdefg"), True)
        self.assertEqual(isUniqueWithCount("abcdefgg"), False)
    
    def test_unique_without_count(self):   
        self.assertEqual(isUniqueWOutCount("abcdefg"), True)
        self.assertEqual(isUniqueWOutCount("abcdefgg"), False)
    
    def test_unique_without_data_structure(self):   
        self.assertEqual(isUniqueNoDataStructure("abcdefg"), True)
        self.assertEqual(isUniqueNoDataStructure("abcdefgg"), False)

if __name__ == '__main__':
    unittest.main()
