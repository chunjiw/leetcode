from typing import List
from heapq import heappop, heappush

class Solution:

    def neighbors(self, m, n, r, c):
        result = []
        for (i, j) in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= i < m and 0 <= j < n:
                result.append((i,j))
        return result

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        queue = [(0,0,0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        while queue:
            t, i, j = heappop(queue)
            for ii, jj in self.neighbors(m, n, i, j):
                if visited[ii][jj]:
                    continue
                tt = 1 + max(t, moveTime[ii][jj])
                if ii == m-1 and jj == n-1:
                    return tt
                visited[ii][jj] = True
                heappush(queue, (tt, ii, jj))

sol = Solution()
print(sol.minTimeToReach([[0,4], [4,4]]))
print(sol.minTimeToReach([[0,0,0,0],[0,0,0,0]]))
print(sol.minTimeToReach([[0,1],[1,2]]))
print(sol.minTimeToReach([[14,89],[19,91]]))
