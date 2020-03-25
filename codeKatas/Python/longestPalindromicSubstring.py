# !/usr/bin/env python

from functools import reduce


def longestPalindrome(substring: str) -> str:
    longest = ""
    for i in range(len(substring)):
        pOdd = getPalindrome(substring, i, i)
        pEven = getPalindrome(substring, i, i + 1)
        longest = reduce(lambda a, b: a if len(a) > len(b) else b, [longest, pOdd, pEven])
    return longest

def getPalindrome(string: str, left: int, right: int) -> str:
    lPointer, rPointer = 0, 0
    while left >= 0 and right < len(string):
        if string[left] == string[right]:
            lPointer, rPointer = left, right
        else:
            break
        left -= 1
        right += 1
    return string[lPointer:rPointer + 1]


if __name__ == "__main__":
    user_input = input('Enter string to find longest palindrome: ')
    print(longestPalindrome(user_input))
