#!/usr/bin/env python

def getChange(coinSet, value):
    numUsedCoins = 0

    while value != 0:
        for coin in coinSet:
            while value - coin >= 0:
                numUsedCoins += 1
                value = value - coin
        break
    return numUsedCoins


