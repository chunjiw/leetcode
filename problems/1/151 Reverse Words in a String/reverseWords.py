class Solution:
    def reverseWords(self, s: str) -> str:
        st = list(s)
        n = len(st)
        i, j = 0, 0
        while j < n:
            while j < n and st[j] == ' ':
                j += 1
            x = i
            while j < n and st[j] != ' ':
                st[i] = st[j]
                i += 1
                j += 1
            y = i - 1
            if i < n and x <= y:
                st[i] = ' '
                i += 1
            while x < y:
                st[x], st[y] = st[y], st[x]
                x += 1
                y -= 1
        if st[i - 1] == ' ':
            i -= 1
        x, y = 0, i - 1
        while x < y:
            st[x], st[y] = st[y], st[x]
            x += 1
            y -= 1
        return ''.join(st[:i])


sol = Solution()
print(sol.reverseWords("  hello world  "))
