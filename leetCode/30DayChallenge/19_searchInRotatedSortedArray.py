"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

"""


# Solution involves iterating through array to find pivot point, and from that pivot point using binary search to find the target

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        
        if nums[0] == target:
            return 0
        
        pivot = len(nums) - 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                pivot = i
        left, right = (0, pivot) if nums[0] < target else (pivot+1, len(nums) - 1)
        
        while left < right:
            print(left, right)
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left += 1
            else:
                right -=1
        return right if nums[right] == target else -1


