class Solution:

    def neighbor(self, i, j, m, n):
        result = []
        for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ii < m and 0 <= jj < n:
                result.append((ii,jj))
        return result

    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        best = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] or grid[i][j] == 0:
                    continue
                visited[i][j] = True
                queue = deque([(i,j)])
                fish = grid[i][j]
                while queue:
                    x, y = queue.popleft()
                    for ii, jj in self.neighbor(x, y, m, n):
                        if not visited[ii][jj] and grid[ii][jj] > 0:
                            queue.append((ii,jj))
                            fish += grid[ii][jj]
                            visited[ii][jj] = True
                best = max(best, fish)
        return best
                