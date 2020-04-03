# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.

# If the target is not found in the array, return [-1, -1].

"""
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

# Binary Search solution in order to keep the run time at O(logN) rather than O(N)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]

        # find any instance of target
        mid = self.searchForTarget(nums, target)

        if mid == -1:
            return [-1, -1]

        left, right = mid, mid

        # get Left Bound
        while left >= 0 and nums[left] == target:
            left -= 1

        # get Right Bound
        while right < len(nums) and nums[right] == target:
            right += 1

        return [left + 1, right - 1]

    def searchForTarget(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1

