class Solution:

    def neighbors(self, i, j, m, n):
        result = []
        for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ii < m and 0 <= jj < n:
                result.append((ii, jj))
        return result

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        frontier = deque([])
        visited = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    isWater[i][j] = m*n
                    frontier.append((i,j))
                    visited[i][j] = 1
        height = 0
        while frontier:
            height += 1
            for _ in range(len(frontier)):
                i, j = frontier.popleft()
                for ii, jj in self.neighbors(i, j, m, n):
                    if not visited[ii][jj]:
                        isWater[ii][jj] = height
                        visited[ii][jj] = 1
                        frontier.append((ii,jj))
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == m*n:
                    isWater[i][j] = 0
        return isWater