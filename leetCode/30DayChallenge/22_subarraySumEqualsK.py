"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""

# Big O is only O(N) because we go through the array only one time

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, sumOfSub = 0, 0
        sums = {}

        sums.update({0:1})
        for i, val in enumerate(nums):
            sumOfSub += val
            if sumOfSub - k in sums:
                count += sums.get(sumOfSub - k)
            sums.update({sumOfSub:sums.get(sumOfSub, 0) + 1})
        return count


