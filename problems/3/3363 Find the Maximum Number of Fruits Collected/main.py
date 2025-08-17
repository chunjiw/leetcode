# algo: DP
# one child must travel diagonal
# other children should not cross diagonal, therefore separate the problem into three sub problems
# TC: O(n^2)
# SC: O(n^2)

class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        n = len(fruits)
        result = sum(fruits[i][i] for i in range(n))
        for i in range(n):
            fruits[i][i] = 0
        grid = [[0] * n for _ in range(n)]

        # start from grid[0][n-1] first
        grid[0][n-1] = fruits[0][n-1]
        for i in range(1, n):
            for j in range(max(i, n-i-1), n):
                grid[i][j] = fruits[i][j] + max(grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1] if j+1 < n else 0)
        result += grid[-1][-1]
        grid[n-1][0] = fruits[n-1][0]
        for i in range(n):
            grid[i][i] = 0
        for i in range(1, n):
            for j in range(max(i, n-i-1), n):
                grid[j][i] = fruits[j][i] + max(grid[j-1][i-1], grid[j][i-1], grid[j+1][i-1] if j+1 < n else 0)
        result += grid[-1][-1]
        return result
    
sol = Solution()
print(sol.maxCollectedFruits([[1,2,3,4], [5,6,8,7], [9,10,11,12], [13,14,15,16]]))