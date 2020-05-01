"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 
"""
class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        dpArray = [[[None, 0, None, None] for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
        for i in range(1, len(str2) + 1):
            for j in range(1, len(str1) + 1):
                if str2[i-1] == str1[j-1]:
                    dpArray[i][j] = [str2[i-1], dpArray[i-1][j-1][1] + 1, i-1, j-1]
                else:
                    if dpArray[i-1][j][1] > dpArray[i][j-1][1]:
                        dpArray[i][j] = [None, dpArray[i-1][j][1], i-1, j]
                        
                    else:
                        dpArray[i][j] = [None, dpArray[i][j-1][1], i, j-1]

        return dpArray[-1][-1][1]

