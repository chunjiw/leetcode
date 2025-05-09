from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for c in coins:
            ndp = dp.copy()
            for i in range(amount + 1):
                d = c
                while i+d <= amount:
                    ndp[i+d] += dp[i]
                    d += c
            dp = ndp
        return dp[amount]

sol = Solution()
print(sol.change(5, [1,2,5]))