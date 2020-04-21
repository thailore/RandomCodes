"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                leastStepsToPoint = grid[i][j]
                # if in middle of grid, choose least steps from either left or above path
                if i > 0 and j > 0:
                    leastStepsToPoint += min(dp[i-1][j], dp[i][j-1])
                # if at left of grid, can only choose from top
                elif i > 0:
                    leastStepsToPoint += dp[i-1][j]
                # if at top of grid, can only choose from left
                elif j > 0:
                    leastStepsToPoint += dp[i][j-1]
                dp[i][j] = leastStepsToPoint
        
        return dp[-1][-1]

