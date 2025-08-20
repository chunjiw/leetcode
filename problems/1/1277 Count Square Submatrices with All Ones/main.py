class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        sl, vl = [0] * (n+1), [0] * n
        psl = sl.copy()
        res = 0
        for row in matrix:
            hl = 0
            for j in range(n):
                if row[j] == 0:
                    vl[j] = hl = sl[j] = 0
                else:
                    sl[j] = 1 + min(vl[j], hl, psl[j-1])
                    vl[j] += 1
                    hl += 1
                    res += sl[j]
            psl, sl = sl, psl
        return res
    
sol = Solution()
print(sol.countSquares([[0,1,1,1], [1,1,1,1], [0,1,1,1]]))