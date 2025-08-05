from collections import deque

class Solution:
    def shortestDistance(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        ds = [(-1,0), (1,0), (0,1), (0,-1)]

        result = m*n*m*n
        for i in range(m):
            for j in range(n):
                # get total travel distance
                if grid[i][j] != 0:
                    continue
                front = deque([ (i,j) ])
                visited = { (i,j) }
                distance = 0
                total = 0
                while front:
                    distance += 1
                    for _ in range(len(front)):
                        r, c = front.popleft()
                        for dr, dc in ds:
                            rr, cc = r+dr, c+dc
                            if 0 <= rr < m and 0 <= cc < n:
                                if grid[rr][cc] == 2 or (rr,cc) in visited:
                                    continue
                                if grid[rr][cc] == 1:
                                    total += distance
                                    # print(i, j, rr, cc, distance, total)
                                else:
                                    front.append((rr,cc))
                                visited.add((rr,cc))
                result = min(result, total)

        return result

sol = Solution()
print(sol.shortestDistance([[1,0,2,0,1], [0,0,0,0,0], [0,0,1,0,0]]))