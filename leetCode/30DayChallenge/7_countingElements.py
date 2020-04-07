# Given an integer array arr, count element x such that x + 1 is also in arr
# If there're duplicates in arr, count them seperately.

"""
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.

Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.
"""

# Used a Hashset solution. Building the hash involves one run through of the array O(N)
# creating the count via the hash lookup has O(1) per hash lookup and the array iteration
# is another O(N).. O(1*N + N + N) == O(3*N) == O(N)

class Solution:
    def countElements(self, arr: List[int]) -> int:
        values = self.buildDict(arr)
        count = 0
        for val in arr:
            exists = values.get(val+1)
            if exists is not None:
                count+=1
        return count

    def buildDict(self, arr: List[int]) -> dict:
        values = {}
        for val in arr:
            count = values.get(val)
            if count is None:
                values.update({val:1})
        return values


