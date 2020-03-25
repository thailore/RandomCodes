#!/usr/bin/env python

import unittest

from main import *

class TestLongestPalindrome(unittest.TestCase):

    def test_longestPalindrome(self):   
        self.assertEqual(longestPalindrome('banana'), 'anana')

if __name__ == '__main__':
    unittest.main()
