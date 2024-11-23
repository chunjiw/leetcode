class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ''
        st = list(s)
        n = len(st)
        isword = False
        i = 0
        for j in range(n):
            if st[j] == ' ':
                if isword:
                    isword = False
                    st[i] = st[j]
                    i += 1
                else:
                    continue
            else:
                isword = True
                st[i] = st[j]
                i += 1
        if st[-1] == ' ':
            i -= 1
        res = st[:i]
        res.reverse()
        if not res:
            return ''
        i = 0
        n = len(res)
        for j in range(n + 1):
            if (j < n and res[j] == ' ') or j == n:
                x, y = i, j - 1
                while x < y:
                    res[x], res[y] = res[y], res[x]
                    x += 1
                    y -= 1
                i = j + 1
        return ''.join(res)

sol = Solution()
print(sol.reverseWords("  hello world  "))
