from typing import List

from heapq import heappush, heappop

class Solution:

    def neighbors(self, r, c, m, n):
        ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = []
        for dr, dc in ds:
            if 0 <= r+dr < m and 0 <= c+dc < n:
                result.append((r+dr, c+dc))
        return result

    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1
        m, n = len(grid), len(grid[0])
        queue = [(0,0,0)]    # time, row, col
        visited = {(0,0)}
        while queue:
            for _ in range(len(queue)):
                time, i, j = heappop(queue)
                for ii, jj in self.neighbors(i, j, m, n):
                    if (ii, jj) not in visited:
                        if grid[ii][jj] <= time+1:
                            ntime = time + 1
                        elif (grid[ii][jj] - time) % 2 != 0:
                            ntime = grid[ii][jj]
                        else:
                            ntime = grid[ii][jj] + 1
                        heappush(queue, (ntime, ii, jj))
                        visited.add((ii, jj))
                        if (ii, jj) == (m-1, n-1):
                            return ntime
        print("should not reach here")
        return -1

sol = Solution()
print(sol.minimumTime([[0,1,3,2],[5,1,2,5],[4,3,8,6]]))
print(sol.minimumTime([[0,2,4],[3,2,1],[1,0,4]]))