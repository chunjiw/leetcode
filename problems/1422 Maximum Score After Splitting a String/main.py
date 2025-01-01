class Solution:
    def maxScore(self, s: str) -> int:
        zeros = ones = 0
        best = -2
        for ch in s[:-1]:
            if ch == '0':
                zeros += 1
            else:
                ones += 1
            best = max(best, zeros - ones)
        if s[-1] == '1':
            ones += 1
        return best + ones