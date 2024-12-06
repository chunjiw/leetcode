class Solution:
    def __init__(self):
        self.ans = [0, 1, 2]

    def climbStairs(self, n: int) -> int:
        if n < len(self.ans):
            return self.ans[n]
        ans = self.climbStairs(n-1) + self.climbStairs(n-2)
        if n == len(self.ans):
            self.ans.append(ans)
        return ans

sol = Solution()
print(sol.climbStairs(44))