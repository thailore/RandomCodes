#! usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import nlargest

def maxNumber(nums1, nums2, k):
    nums = nums1
    for c in nums2:
        nums.append(c)
    return nlargest(int(k), nums)



if __name__ == '__main__':
    nums1 = input("Enter nums1 sep. by commas: ")
    nums1 = nums1.split(',')
    for index, val in enumerate(nums1):
        nums1[index] = int(val)
    nums2 = input("Enter nums2 sep. by commas: ")
    nums2 = nums2.split(',')
    for index, val in enumerate(nums2):
        nums2[index] = int(val)
    k = input("Enter amount of highest numbers to find: ")
    print(maxNumber(nums1, nums2, k))





