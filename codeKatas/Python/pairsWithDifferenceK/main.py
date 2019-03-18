#!/usr/bin/env python

def numberOfPairsWithDifferenceK(numbers, difference):
    k = difference
    numberHash = dict()
    for number in numbers:
        numberHash.update({number:True})
    numberOfPairs = 0
    for number in numbers:  
        result = numberHash.get(number+k, False)
        if result == True:
            numberOfPairs+=1
    return numberOfPairs


