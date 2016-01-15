#! usr/bin/env python
# -*- coding: utf-8 -*-

"""You are given coins of different denominations and a total amount of
money amount. Write a function to compute the fewest number of coins
that you need to make up that amount.
"""

def coinChange(coins, amount):
    coins = sorted(coins)
    amount = int(amount)
    grouping = []
    total = 0

    while amount != 0:
        for i in range(len(coins)):
            #try to get highest value in sorted array first
            j = len(coins) - (i + 1)
            while amount >= coins[j]:
                #if subtracting coin value gets you to negative
                if amount - coins[0] < 0:
                    return -1
                elif amount-coins[j] < 0:
                    break
                else:
                    amount -= coins[j]
                    grouping.append(coins[j])
                    total += 1
    print("Coin set used: {}".format(grouping))
    return total


if __name__ == '__main__':
    
    coins = input("Enter coin values separated by , : ")
    coins = coins.split(',')
    for index, val in enumerate(coins):
        coins[index] = int(val)

    amount = input("Enter amount: ")
    print("Needs {0} coins".format(coinChange(coins, amount)))

    
