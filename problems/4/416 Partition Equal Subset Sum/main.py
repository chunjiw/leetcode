from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s //= 2
        dp = [0] * (s+1)
        dp[0] = 1    # there is 1 way to get subset that sums to 0
        for num in nums:
            ndp = dp.copy()
            for i in range(s+1):
                if i + num <= s:
                    ndp[i + num] += dp[i]
                if ndp[s] > 0: 
                    return True
            dp = ndp
        return False

sol = Solution()
print(sol.canPartition([1,5,11,5]))