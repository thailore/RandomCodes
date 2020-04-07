"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.
"""

"""
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # linear solution includes finding K closest numbers and then just checking if those numbers are in the array... 
        # that would be at O(K*N)

        # binary search solution includes finding K closest numbers and then searching via binary search
        # results in O(K*logN)

        # find the difference between each number and value x, then sort those values in an array based on the difference. 
        # return the first K numbers of that array .. 
        # depending on the how its sorted it could be linear for the differences N + NlogN for the sorting... == NlogN

        sortedByDiff = sorted(arr, key=lambda num: abs(num - x))
        return sorted(sortedByDiff[:k])

