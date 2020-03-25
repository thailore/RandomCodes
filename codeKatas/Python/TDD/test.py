#!/usr/bin/env python

"""
test.py
"""

import unittest

from main import *

class TestDrivenDevelopment(unittest.TestCase):

	def test_pythagorean_theroem(self):
		a, b = 3, 4
		self.assertEqual(calculate_side_c(a, b), 5)

if __name__ == '__main__':
    unittest.main()
