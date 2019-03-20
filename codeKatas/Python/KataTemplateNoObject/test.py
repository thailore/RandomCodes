#!/usr/bin/env python

import unittest

from main import *

class TestKata(unittest.TestCase):

    def test_upper(self):   
        self.assertEqual(test(), True)

if __name__ == '__main__':
    unittest.main()
