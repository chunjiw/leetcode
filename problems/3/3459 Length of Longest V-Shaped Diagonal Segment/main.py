class Solution:
    def lenOfDiagonal(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def isseq(x, y):
            return x*y == 0 and x+y == 2
        
        def ishead(x):
            return x == 0 or x == 2

        def getDP(grid):
            a = [[0]*n for _ in range(m)]   # upper right to lower left
            for k in range(0, m+n-1):       # loop over sum of indices, 0 <= i <= m-1, 0 <= j <= n-1 
                for i in range(max(0, k-n+1), min(k+1, m)):
                    j = k - i
                    if j+1 < n and i-1 >= 0 and isseq(grid[i][j], grid[i-1][j+1]):
                        a[i][j] = a[i-1][j+1] + 1
                    elif ishead(grid[i][j]):
                        a[i][j] = 1
            
            c = [[0]*n for _ in range(m)]   # lower left to upper right
            for k in range(0, m+n-1):       # loop over sum of indices, 1 <= i <= m-1, 0 <= j <= n-2
                for j in range(max(0, k-m+1), min(k+1, n)):
                    i = k - j
                    if j-1 >= 0 and i+1 < m and isseq(grid[i][j], grid[i+1][j-1]):
                        c[i][j] = c[i+1][j-1] + 1
                    elif ishead(grid[i][j]):
                        c[i][j] = 1
            return a, c

        a, c = getDP(grid)

        rrid = [list(reversed(row)) for row in grid]

        rb, rd = getDP(rrid)

        b = [list(reversed(row)) for row in rb]        
        d = [list(reversed(row)) for row in rd]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                res = max(res, 1)
                # explore 4 directions to see possible solutions
                # direction a
                if i-1 >= 0 and j+1 < n and grid[i-1][j+1] == 2:
                    for k in range(a[i-1][j+1]):
                        res = max(res, 1 + d[i-1-k][j+1+k] + k)                        
                # direction b
                if i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] == 2:
                    for k in range(b[i-1][j-1]):
                        res = max(res, 1 + a[i-1-k][j-1-k] + k)                        
                # direction c
                if i+1 < m and j-1 >= 0 and grid[i+1][j-1] == 2:
                    for k in range(c[i+1][j-1]):
                        res = max(res, 1 + b[i+1+k][j-1-k] + k)                        
                # direction d
                if i+1 < m and j+1 < n and grid[i+1][j+1] == 2:
                    for k in range(d[i+1][j+1]):
                        res = max(res, 1 + c[i+1+k][j+1+k] + k)                        
        
        # for row in a:
        #     print(row)
        # print()
        # for row in d:
        #     print(row)


        return res
        

sol = Solution()
print(sol.lenOfDiagonal([[2,2,1,2,2], [2,0,2,2,0], [2,0,1,1,0], [1,0,2,2,2], [2,0,0,2,2]]))
print(sol.lenOfDiagonal([[2,2,2,2,2], [2,0,2,2,0], [2,0,1,1,0], [1,0,2,2,2], [2,0,0,2,2]]))
print(sol.lenOfDiagonal([[1,2,2,2,2], [2,2,2,2,0], [2,0,0,0,0], [0,0,2,2,2], [2,0,0,2,0]]))
print(sol.lenOfDiagonal([[1]]))
print(sol.lenOfDiagonal([[2,2,0,2,0,2,0], [1,2,2,1,0,2,0]]))
