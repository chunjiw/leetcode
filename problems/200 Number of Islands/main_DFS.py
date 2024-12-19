from typing import List

class Solution:

    def neighbors(self, i, j, m, n):
        result = []
        for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= r < m and 0 <= c < n:
                result.append((r, c))
        return result

    def recursiveFlood(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        grid[i][j] = '0'
        for ii, jj in self.neighbors(i, j, m, n):
            if grid[ii][jj] == '1':
                self.flood(grid, ii, jj)

    def iterativeFlood(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        stack = [(i, j)]
        grid[i][j] = '0'
        while stack:
            i, j = stack.pop()
            for ii, jj in self.neighbors(i, j, m, n):
                if grid[ii][jj] == '1':
                    grid[ii][jj] = '0'
                    stack.append((ii, jj))

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.iterativeFlood(grid, i, j)
                    count += 1
        return count

sol = Solution()
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
sol.iterativeFlood(grid, 0, 0)
print(grid)