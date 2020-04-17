"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        calcValues = [amount + 1 for _ in range(amount + 1)]
        calcValues[0] = 0
        i = 0
        while i <= amount:
            minimum = calcValues[i]
            for coin in coins:
                if coin <= i:
                    minimum = min(calcValues[i - coin] + 1, minimum)
                    calcValues[i] = minimum
            i += 1
        answer = calcValues[amount]
        return answer if answer != amount + 1 else -1

