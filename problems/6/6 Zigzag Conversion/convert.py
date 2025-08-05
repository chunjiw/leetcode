class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ''
        if numRows == 1:
            return s
        n = len(s)
        res = []
        for row in range(numRows):
            i = row
            while i < n:
                res.append(s[i])
                if row != 0 and row != numRows - 1 and i + 2*(numRows-row) - 2 < n:
                    res.append(s[i + 2*(numRows-row) - 2])
                i += numRows + numRows - 2
        return ''.join(res)

sol = Solution()
print(sol.convert('PAYPALISHIRING', 3))