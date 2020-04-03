# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

"""
Input: [2,2,1]
Output: 1

Input: [4,1,2,1,2]
Output: 4
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = {}
        for i in nums:
            if answer.get(i) is not None:
                answer.pop(i)
            else:
                answer.update({i:i})
        return next(iter(answer))
