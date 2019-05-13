#! usr/bin/env python
# -*- coding: utf-8 -*-

"""Reverse C style string"""

def reversed_string(string_input):
	reversed = string_input[::-1]
	return reversed


if __name__ == '__main__':
	string_input = input("Enter a string to be reversed: ")
	print("{0} reversed is {1}".format(string_input, reversed_string(string_input)))