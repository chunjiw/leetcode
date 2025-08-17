class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j > 0:
                    dp[j] = dp[j-1] and s3[i+j-1] == s2[j-1]
                elif i > 0:
                    if j == 0:
                        dp[j] = dp[j] and s3[i+j-1] == s1[i-1]
                    else:
                        dp[j] = (dp[j-1] and s3[i+j-1] == s2[j-1]) or (dp[j] and s3[i+j-1] == s1[i-1])
        return dp[-1]

