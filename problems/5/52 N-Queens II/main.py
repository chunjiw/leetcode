class Solution:

    def build(self, m, n, occupied):
        if m == n:
            self.count += 1
            return
        for i in range(n):
            if i in occupied[0] or m - i in occupied[1] or m + i in occupied[2]:
                continue
            occupied[0].add(i)
            occupied[1].add(m - i)
            occupied[2].add(m + i)
            self.build(m + 1, n, occupied)
            occupied[0].remove(i)
            occupied[1].remove(m - i)
            occupied[2].remove(m + i)
            
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.build(0, n, [set() for _ in range(3)])
        return self.count

sol = Solution()
print(sol.totalNQueens(4))