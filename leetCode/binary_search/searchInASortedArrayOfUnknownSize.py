# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 1
        while reader.get(right) <= target:
            right *= 2
        
        while left <= right:
            print(left, right)
            mid = (left + right) // 2
            val = reader.get(mid)
            if val == target:
                return mid
            if val > target:
                right = mid - 1
            if val < target:
                left = mid + 1
        return -1

