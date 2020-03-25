#!/usr/bin/env python

import unittest

from main import *

class TestCompression(unittest.TestCase):

    def test_compression(self):   
        self.assertEqual(compressDecompress('10[a]'), 'aaaaaaaaaa')
	self.assertEqual(compressDecompress('3[abc]4[ab]c'), 'abcabcabcababababc')

if __name__ == '__main__':
    unittest.main()
