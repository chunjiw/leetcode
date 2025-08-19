class Solution:
    
    def iterate(self, n: int, k: int, maxPts: int) -> float:

        p = [0] * (n+1)
        p[0] = 1

        result = sum(p[i] for i in range(k, n+1))

        # O(k)
        for _ in range(k):
            for i in range(k, n+1):
                p[i] = 0
            curr_sum = sum(p[ max(0,n-maxPts) : n])
            p[n] = curr_sum / maxPts
            # O(n)
            for i in range(n-1, -1, -1):
                curr_sum -= p[i]
                if i-maxPts >= 0:
                    curr_sum += p[i-maxPts]
                p[i] = curr_sum / maxPts
            result += sum(p[i] for i in range(k, n+1))
            print([f"{abs(x):.2f}" for x in p])
        return result
    
    def onepass(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, maxPts + 1):
                if i - j >= 0 and i - j < k:
                    dp[i] += dp[i - j] / maxPts
        print([f"{abs(x):.2f}" for x in dp])
        return sum(dp[k:])

sol = Solution()
print(sol.iterate(10, 7, 3))
print(sol.onepass(10, 7, 3))