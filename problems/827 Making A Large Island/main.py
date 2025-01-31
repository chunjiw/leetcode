class Solution:

    def neighbor(self, i, j, n):
        result = []
        for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ii < n and 0 <= jj < n:
                result.append((ii,jj))
        return result

    def largestIsland(self, grid: List[List[int]]) -> int:
        # label island with its size
        n = len(grid)
        rep = [[None for _ in range(n)] for _ in range(n)]
        result = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] <= 0:
                    continue
                # label a new island: get size
                stack = [(i,j)]
                grid[i][j] = -1
                rep[i][j] = (i,j)
                size = -1
                while stack:
                    r, c = stack.pop()
                    for rr, cc in self.neighbor(r, c, n):
                        if grid[rr][cc] == 1:
                            stack.append((rr,cc))
                            grid[rr][cc] = -1
                            rep[rr][cc] = (i,j)
                            size -= 1
                # label a new island: label size
                stack = [(i,j)]
                grid[i][j] = size
                result = max(result, -size)
                while stack:
                    r, c = stack.pop()
                    for rr, cc in self.neighbor(r, c, n):
                        if grid[rr][cc] == -1:
                            stack.append((rr,cc))
                            grid[rr][cc] = size
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    pot = 1
                    counted = set()
                    for ii, jj in self.neighbor(i, j, n):
                        if grid[ii][jj] < 0 and rep[ii][jj] not in counted:
                            pot -= grid[ii][jj]
                            counted.add(rep[ii][jj])
                    result = max(result, pot)
        return result
