class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s //= 2
        # pick a subset that sums to s
        dp = [False] * (s+1)
        dp[0] = True    # without any number in the subset, a sum of 0 is achievable
        for i in range(0, len(nums)):
            ndp = list(dp)
            for j in range(0, s+1):
                if dp[j] and j+nums[i] <= s:
                    ndp[j+nums[i]] = True    # if j is achievable, then j + nums[i] is also achievable
            dp = ndp
            if dp[s]:
                return True
        return False