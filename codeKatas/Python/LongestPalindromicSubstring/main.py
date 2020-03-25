#!/usr/bin/env python

def longestPalindrome(substring):
    rSubstring = substring[::-1]
    longest = substring[0] if len(substring) > 0 else ""
    new = ""
    for i, char in enumerate(substring):
        if substring[i] == rSubstring[i]:
            new += char
        else:
            if len(new) > len(longest):
                longest = new
            new = ""

    return longest if len(longest) > len(new) else new

