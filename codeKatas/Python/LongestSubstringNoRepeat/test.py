#!/usr/bin/env python

import unittest

from main import *

class TestLongestSubstringNoRepeat(unittest.TestCase):

    def test_lengthOfLongestSubstring(self):   
        self.assertEqual(lengthOfLongestSubstring('abrkaabcdefghijjxxxi'), 10)

if __name__ == '__main__':
    unittest.main()
