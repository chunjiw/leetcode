class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        result = 0
        left = 0
        i = 0
        while i < n:
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                # insert ')' if not double '))'
                if i+1 == n or s[i+1] != ')':
                    result += 1
                else:
                    i += 1
                # here, treat it as regular closing parenthesis
                if left > 0:
                    left -= 1
                else:
                    result += 1
            i += 1
        return result + left * 2