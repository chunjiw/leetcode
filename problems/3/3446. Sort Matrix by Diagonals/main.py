class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        
        n = len(grid)

        # loop over k = i-j
        for k in range(n):
            arr = [grid[k+j][j] for j in range(n-k)]
            arr.sort(reverse=True)
            for j in range(0, n-k):
                grid[k+j][j] = arr[j]
        
        # loop over k = j-i
        for k in range(1, n):
            arr = [grid[i][i+k] for i in range(n-k)]
            arr.sort()
            for i in range(n-k):
                grid[i][i+k] = arr[i]

        return grid        
