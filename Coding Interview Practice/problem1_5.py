#! usr/bin/env python
# -*- coding: utf-8 -*-

def replace_space(s1):
	s1 = s1.replace(' ','%20')
	return s1


if __name__ == '__main__':
	s1 = input("Enter a string: ")
	print("New string is: {}".format(replace_space(s1)))
