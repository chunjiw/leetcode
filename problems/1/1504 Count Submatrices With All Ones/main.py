class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        streak = [[0]*(n+1) for _ in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                long = streak[i][j] = streak[i][j-1] + 1
                for k in range(i, -1, -1):
                    long = min(long, streak[k][j])
                    result += long
        return result
    
sol = Solution()
print(sol.numSubmat([[1,0,1], [1,1,0], [1,1,0]]))