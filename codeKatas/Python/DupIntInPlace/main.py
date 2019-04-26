#!/usr/bin/env python

def findBiggestNumWithDupInts(value):
    stringedNumber = str(value)
    highest = 0
    
    for num in range(1, len(stringedNumber)+1):
        tempVersion = int(stringedNumber[:num] + stringedNumber[num-1] + stringedNumber[num:])
        if tempVersion > highest:
            highest = tempVersion
    return highest



