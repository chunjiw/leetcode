class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalsum = sum(nums)
        if target < -totalsum or totalsum < target:
            return 0
        offset = totalsum
        sumcount = [0 for _ in range(2*totalsum+1)]
        # initial condition
        sumcount[offset + nums[0]] += 1
        sumcount[offset - nums[0]] += 1
        for i in range(1, len(nums)):
            next_dp = list(sumcount)
            num = nums[i]
            for s in range(0, num):
                next_dp[s] = sumcount[s+num]
            for s in range(num, 2*totalsum+1-num):
                next_dp[s] = sumcount[s-num] + sumcount[s+num]
            for s in range(2*totalsum+1-num, 2*totalsum+1):
                next_dp[s] = sumcount[s-num]
            sumcount = next_dp
        return sumcount[offset + target]