# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.

"""
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal = nums[0]
        subArraySum = 0
        for i in range(0, len(nums)):
            subArraySum = max(nums[i], subArraySum + nums[i])
            maxVal = max(maxVal, subArraySum)
        return maxVal

