class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dpCol = [[0] * n for _ in range(m)]
        dpRow = [[0] * n for _ in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                if j == 0:
                    dpCol[i][j] = 1
                else:
                    dpCol[i][j] = dpCol[i][j-1] + 1
                if i == 0:
                    dpRow[i][j] = 1
                else:
                    dpRow[i][j] = dpRow[i-1][j] + 1
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j-1] + 1, dpCol[i][j], dpRow[i][j])
                else:
                    dp[i][j] = 1
                result = max(result, dp[i][j] * dp[i][j])
        return result
        