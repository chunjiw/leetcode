class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        profit_map = [[0] * n for _ in range(n)]
        for i in range(n):
            prev_min = prices[i]
            best = 0
            for j in range(i+1, n):
                profit_map[i][j] = max(profit_map[i][j-1], prices[j] - prev_min)
                prev_min = min(prev_min, prices[j])
        dp = [profit_map[0].copy() for _ in range(k)]
        for i in range(1, k):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]
                for d in range(1, j-1):
                    dp[i][j] = max(dp[i][j], dp[i-1][d] + profit_map[d+1][j])
        return max(dp[k-1])
