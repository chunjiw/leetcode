def maxPathSum(grid):
    n = len(grid)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(n):
        for j in range(n):
            if i > 0 and j > 0:
                dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1])
            elif i > 0:
                dp[i][j] = grid[i][j] + dp[i-1][j]
            elif j > 0:
                dp[i][j] = grid[i][j] + dp[i][j-1]
    return dp[-1][-1]
                
for _ in range(int(input())):
    n, q = [int(i) for i in input().split()]
    grid = [[int(i) for i in input().split()] for _ in range(n)]
    seen = set()
    for _ in range(q):
        k, v = [int(i) for i in input().split()]
        k -= 2
        for i in range(n):
            j = k - i
            if 0 <= i < n and 0 <= j < n:
                pv = grid[i][j]
                grid[i][j] = v
        if k not in seen:
            mps = maxPathSum(grid)
            print(mps)
            seen.add(k)
        else:
            mps += v - pv
            print(mps)