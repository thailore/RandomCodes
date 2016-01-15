#! usr/bin/env python
# -*- coding: utf-8 -*-

"""Check if inputted string has all unique characters"""

def is_unique(string_input):
	check = []
	for c in string_input:
		if c in check:
			return False
		else:
			check.append(c)
	return True

if __name__ == '__main__':
	string_input = input("Enter a string: ")
	print("Is unique?: {}".format(is_unique(string_input)))
