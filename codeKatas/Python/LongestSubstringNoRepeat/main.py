#!/usr/bin/env python

def lengthOfLongestSubstring(substring):
    leftWindow, rightWindow = 0 ,1
    longest = 0
    while rightWindow <= len(substring):
        stringToCheck = substring[leftWindow:rightWindow]	
        if len(set(stringToCheck)) == len(stringToCheck):
            longest = len(stringToCheck)
            rightWindow += 1
        else:
            leftWindow += 1
            rightWindow += 1
    return longest

