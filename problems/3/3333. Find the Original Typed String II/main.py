class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        rep = []
        prev = word[0]
        count = 1
        for ch in word[1:]:
            if prev == ch:
                count += 1
            else:
                rep.append(count)
                count = 1
            prev = ch
        rep.append(count)

        MOD = 10**9 + 7

        total = 1
        for r in rep:
            total = total * r % MOD

        if len(rep) >= k:
            return total

        # dynamic programming
        # i: index of rep
        # j: number of characters taken so far. So max(j) == k - 1
        n = k
        dp = [0] * n
        dp[0] = 1    # there is 1 way to take zero from empty
        dp_sum = [1] * n
        dp_sum.append(0)    # so that dp_sum[-1] = 0
        ndp = dp.copy()
        ndp_sum = dp_sum.copy()
        for r in rep:
            for j in range(n):
                ndp[j] = 0
                if j-1 >= 0:
                    ndp[j] = dp_sum[j-1]
                    if j-r-1 >= 0:
                        ndp[j] -= dp_sum[j-r-1]
                ndp[j] %= MOD
                ndp_sum[j] = (ndp_sum[j-1] + ndp[j]) % MOD
            dp, ndp = ndp, dp
            dp_sum, ndp_sum = ndp_sum, dp_sum

        return (total - dp_sum[-2]) % MOD
        