class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        col, plus, minus = set(), set(), set()
        result, solution = [], []

        row = ['.'] * n

        def place(i):
            if i == n:
                result.append(solution.copy())
                return
            for j in range(n):
                if j not in col and i+j not in plus and i-j not in minus:  
                    row[j] = 'Q'
                    solution.append(''.join(row))
                    row[j] = '.'
                    col.add(j), plus.add(i+j), minus.add(i-j)
                    place(i+1)
                    col.remove(j), plus.remove(i+j), minus.remove(i-j)
                    solution.pop()
        
        place(0)
        return result

sol = Solution()
print(sol.solveNQueens(4))