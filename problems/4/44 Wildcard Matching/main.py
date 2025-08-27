from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        ns = len(s)
        np = len(p)

        @cache
        def isMatch(i, j) -> bool:
            if i == ns:
                return all(p[k] == '*' for k in range(j, np))
            if j == np:
                return i == ns
            if p[j] != '*':
                return (p[j] == '?' or p[j] == s[i]) and isMatch(i+1, j+1)
            else:
                return any(isMatch(k, j+1) for k in range(i, ns+1))
            
        return isMatch(0, 0)

sol = Solution()
print(sol.isMatch('aa', 'a'))
print(sol.isMatch('a', 'aa'))
print(sol.isMatch('aa', '*'))
print(sol.isMatch('cb', '?a'))
print(sol.isMatch('adceb', '*a*b'))
print(sol.isMatch('acdcb', 'a*c?b'))
