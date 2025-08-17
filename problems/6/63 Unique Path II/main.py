class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = 1
                elif obstacleGrid[i][j]:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        return dp[-1]