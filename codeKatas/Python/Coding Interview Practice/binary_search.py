#! usr/bin/env python
# -*- coding: utf-8 -*-

def binary_search(alist, item):
	if len(alist) == 0:
		return False
	else:
		alist.sort()
		mid = len(alist)//2
		if alist[mid] == item:
			return True
		else:
			if item<alist[mid]:
				return binary_search(alist[:mid],item)
			else:
				return binary_search(alist[mid+1:],item)

if __name__ == '__main__':
	alist = [0,1,5,6,2,7,3,9,4,0,11,20,19,46]
	item = input("Enter a number to be searched for: ")
	print("Is in list: {}".format(binary_search(alist,int(item))))
