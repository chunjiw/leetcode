class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                profit[i][j] = max(prices[j] - prices[i], 0)
        profit1 = [0] * n
        for j in range(n):
            for i in range(0, j):
                profit1[j] = max(profit1[j], profit[i][j])
        profit2 = [0] * n
        for j in range(n-2, -1, -1):
            profit2[j] = max(profit2[j+1], max(profit[j]))
        result = 0
        for i in range(n):
            result = max(result, profit1[i] + profit2[i])
        return result