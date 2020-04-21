"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        first = self.buildString(S)
        second = self.buildString(T)
        return first == second

    def buildString(self, s: str) -> str:
        string = []
        for val in s:
            if val == "#":
                if len(string) > 0:
                    string.pop()
            else:
                string.append(val)
        return "".join(string)

