class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        n = len(haystack)
        m = len(needle)
        if needle == haystack:
            return 0
        for i in range(n - m + 1):
            j = 0
            while j < m and needle[j] == haystack[i + j]:
                j += 1
            if j == m:
                return i
        return -1

sol = Solution()
print(sol.strStr('abc', 'c'))