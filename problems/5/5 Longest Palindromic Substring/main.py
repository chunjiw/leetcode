class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [0] * n
        result = ""
        longest = 0
        for j in range(0, n):
            # here, dp[i] is length of palindrome s[i:j] (not including s[j])
            for i in range(0, j+1):
                if i == j:
                    dp[i] = 1
                # if s[i+1:j] is palindrome, then s[i:j+1] is also palindrome
                elif s[i] == s[j] and (i+1 == j or dp[i+1] > 0):
                    dp[i] = dp[i+1] + 2
                else:
                    dp[i] = 0
                if dp[i] > longest:
                    longest = dp[i]
                    result = s[i:j+1]
            # here, dp[i] is length of palindrome s[i:j+1] (including s[j])
        return result