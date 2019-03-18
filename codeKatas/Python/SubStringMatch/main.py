#!/usr/bin/env python

def isThere(string, subString):
    subStringLength = len(subString)
    endPoint = len(string) - (subStringLength)
    for index in range(endPoint+1):
        offset = index+subStringLength
        if string[index:offset] == subString:
            return True
    return False


