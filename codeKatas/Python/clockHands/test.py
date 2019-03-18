#!/usr/bin/env python

import unittest

from main import *

class TestKata(unittest.TestCase):

    def test_clockHands_0(self):   
        self.assertEqual(getClockhands("12:00"), 0)

    def test_clockHands_165(self):   
        self.assertEqual(getClockhands("12:30"), 165)

    def test_clockHands_180(self):   
        self.assertEqual(getClockhands("6:00"), 180)

    def test_clockHands_90(self):   
        self.assertEqual(getClockhands("9:00"), 90)

    def test_clockHands_75(self):   
        self.assertEqual(getClockhands("3:30"), 75)

if __name__ == '__main__':
    unittest.main()
