class Solution:
    def minimizeResult(self, expression: str) -> str:
        s = expression
        n = len(s)
        c = s.index('+')
        left = [(1, int(s[0:c]))]
        best = int(s[0:c]) + int(s[c+1:])
        result = '(' + s + ')'
        for i in range(1, c):
            left.append((int(s[0:i]), int(s[i:c])))
        right = [(int(s[c+1:]),1)]
        for i in range(1, n-c-1):
            right.append((int(s[c+1:-i]), int(s[-i:])))
        for i, (a, b) in enumerate(left):
            for j, (c, d) in enumerate(right):
                curr = a * (b+c) * d
                if curr < best:
                    best = curr
                    result = f"({b}+{c})"
                    if i != 0:
                        result = str(a) + result
                    if j != 0:
                        result += str(d)
        return result