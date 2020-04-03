# A happy number is a number defined by the following process: 
# Starting with any positive integer, replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers.

"""
Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        s = self.sumOfSquares(n)
        times = 1
        while s != 1:
            if times > 10:
                break
            s = self.sumOfSquares(s)
            times += 1        
        if s == 1:
            return True
        else:
            return False
        
    def sumOfSquares(self, n: int) -> int:
        total = 0
        
        for numChar in str(n):
            total += int(numChar) ** 2
        return total
