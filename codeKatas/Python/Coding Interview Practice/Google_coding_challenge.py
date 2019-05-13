#! usr/bin/env python
# -*- coding: utf-8 -*-

"""The code that got me an interview with google
given a number, duplicate each digit in place once, find the greatest
number possible doing said processs.
Ex: 1234 -> 11234, 12234, 12334, 12344. Should return 12344
"""

def solution(X):
    temp = str(X)
    highest_num = 0
    num_string = list(temp)
    #make copy of num_string using tuple
    #copying another way points to same reference point
    num_string_test = tuple(num_string)
    num_string_test = list(num_string_test)
    for index, val in enumerate(num_string):
        num_string_test.insert(index, val)
        num_string_test = ''.join(num_string_test)
        if highest_num < int(num_string_test):
            highest_num = int(num_string_test)
        num_string_test = tuple(num_string)
        num_string_test = list(num_string_test)
    return highest_num
    


if __name__ == '__main__':
	X = 12515
	print(solution(X))
