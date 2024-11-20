# 200. Number of Islands

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        M = len(grid)
        N = len(grid[0])
        self.result = 0
        visited = [[False for _ in range(N)] for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if self.visit(i, j, M, N, visited, grid):
                    self.result += 1
        return self.result

    def visit(self, i, j, M, N, visited, grid):
        if visited[i][j]:
            return
        visited[i][j] = True
        if grid[i][j] == '0':
            return
        for (ni, nj) in self.neighbor(i, j, M, N):
            self.visit(ni, nj, M, N, visited, grid)
        return True

    def neighbor(self, i, j, M, N):
        nei = []
        if i > 0:
            nei.append((i - 1, j))
        if i < M - 1:
            nei.append((i + 1, j))
        if j > 0:
            nei.append((i, j - 1))
        if j < N - 1:
            nei.append((i, j + 1))
        return nei