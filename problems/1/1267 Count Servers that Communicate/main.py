class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        for i in range(m):
            rowcount = sum(grid[i])
            if rowcount > 1:
                result += rowcount
                for j in range(n):
                    if grid[i][j] == 1:
                        grid[i][j] = 2
        for j in range(n):
            colcount = 0
            for i in range(m):
                if grid[i][j] != 0:
                    colcount += 1
            if colcount > 1:
                for i in range(m):
                    if grid[i][j] == 1:
                        result += 1
        return result