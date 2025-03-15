class Solution:

    def lps(self, s, i, j, prev):
        if i > j:
            return 0
        if i == j:
            return 0
        if (i,j,prev) in self.map:
            return self.map[(i,j,prev)]
        if s[i] == s[j]:
            if s[i] == prev:
                self.map[(i,j,prev)] = self.lps(s, i+1, j-1, prev)
            else:
                self.map[(i,j,prev)] = 2 + self.lps(s, i+1, j-1, s[i])
        else:
            self.map[(i,j,prev)] = max(self.lps(s, i+1, j, prev), self.lps(s, i, j-1, prev))
        return self.map[(i,j,prev)]

    def longestPalindromeSubseq(self, s: str) -> int:
        self.map = dict()
        return self.lps(s, 0, len(s)-1, '#')