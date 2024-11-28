from typing import List

import sys
from collections import deque

class Solution:
    def neighbors(self, r, c, m, n):
        result = []
        if r - 1 >= 0:
            result.append((r-1, c))
        if r + 1 < m:
            result.append((r+1, c))
        if c - 1 >= 0:
            result.append((r, c-1))
        if c + 1 < n:
            result.append((r, c+1))
        return result

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        distances = [[sys.maxsize for _ in range(n)] for _ in range(m)]
        distances[0][0] = 0
        queue = deque([(0, 0)])
        while queue:
            i, j = queue.popleft()
            for (ii, jj) in self.neighbors(i, j, m, n):
                curr_dist = distances[i][j] + grid[ii][jj]
                if curr_dist < distances[ii][jj]:
                    distances[ii][jj] = curr_dist
                    queue.append((ii, jj))
        return distances[m-1][n-1]

sol = Solution()
print(sol.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))