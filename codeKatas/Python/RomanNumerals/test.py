#!/usr/bin/env python

import unittest

from main import *

class TestKata(unittest.TestCase):

    def test_1_plus_2(self):   
        self.assertEqual(romanNumeralsAdd(["I" , "II"]), "III")
        
    def test_2_plus_3(self):   
        self.assertEqual(romanNumeralsAdd(["II" , "III"]), "V")
  
    def test_5_plus_5(self):   
        self.assertEqual(romanNumeralsAdd(["V" , "V"]), "X")
  
    def test_2_plus_3_plus_5(self):   
        self.assertEqual(romanNumeralsAdd(["II" , "III", "V"]), "X")
   
    def test_3_plus_5(self):   
        self.assertEqual(romanNumeralsAdd(["III", "V"]), "VIII")

    def test_2_plus_2(self):
        self.assertEqual(romanNumeralsAdd(["II", "II"]), "IV")
    
    def test_6_plus_5(self):
        self.assertEqual(romanNumeralsAdd(["VI", "V"]), "XI")

    def test_6_plus_3(self):
        self.assertEqual(romanNumeralsAdd(["VI", "II"]), "IX")

if __name__ == '__main__':
    unittest.main()
