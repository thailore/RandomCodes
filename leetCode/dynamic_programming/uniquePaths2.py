"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                numPaths = 0
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        numPaths = 1
                    elif i > 0 and j > 0:
                        numPaths += dp[i-1][j] + dp[i][j-1]
                    elif i > 0:
                        numPaths += dp[i-1][j]
                    elif j > 0:
                        numPaths += dp[i][j-1]

                    dp[i][j] = numPaths
        return dp[-1][-1]
