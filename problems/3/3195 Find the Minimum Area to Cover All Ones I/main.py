class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        lef, rit, top, bot = n, -1, m, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    lef = min(lef, j)
                    rit = max(rit, j)
                    top = min(top, i)
                    bot = max(bot, i)
        if lef > rit:
            return 0
        return (rit-lef+1) * (bot-top+1)

sol = Solution()
print(sol.minimumArea([[1,0,1], [0,1,0]]))
print(sol.minimumArea([[1,0], [0,0]]))