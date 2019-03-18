#!/usr/bin/env python
import unittest

from main import *

class SubStringTest(unittest.TestCase):

    def test_canRetrieveSubString(self):   
        self.assertEqual(isThere("abcdeyesab", "yes"), True)

if __name__ == '__main__':
    unittest.main()
