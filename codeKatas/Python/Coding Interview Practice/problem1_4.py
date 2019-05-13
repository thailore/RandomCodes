#! usr/bin/env python
# -*- coding: utf-8 -*-

"""Checks if two strings are anagrams of each other"""

def is_anagram(s1, s2):
	s1 = list(s1)
	s1.sort()
	s2 = list(s2)
	s2.sort()
	if s1 == s2:
		return True
	else:
		return False

if __name__ == '__main__':
	s1 = input("Enter first string: ")
	s2 = input("Enter second string: ")

	print("Anagrams? {}".format(is_anagram(s1,s2)))