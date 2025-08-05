from collections import Counter

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m = len(target)
        n = len(words[0])
        modulo = 1000000007
        dp = [0] * n
        counts = [Counter([word[j] for word in words]) for j in range(n)]
        dp[-1] = counts[-1][target[-1]] % modulo
        for j in range(-2, -n-1, -1):
            dp[j] = (dp[j+1] + counts[j][target[-1]]) % modulo
        for i in range(-2, -m-1, -1):
            ndp = [0] * n
            for j in range(-2, -n-1, -1):
                ndp[j] = (ndp[j+1] + dp[j+1] * counts[j][target[i]]) % modulo
            dp = ndp
        return dp[0]
