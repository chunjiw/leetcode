class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalsum = sum(nums)
        if target < -totalsum or totalsum < target:
            return 0
        offset = totalsum
        sumcount = [[0 for _ in range(2*totalsum+1)] for _ in range(len(nums))]
        for i, num in enumerate(nums):
            if i == 0:
                sumcount[0][offset + num] += 1
                sumcount[0][offset - num] += 1
                continue
            for s in range(num, 2*totalsum+1):
                sumcount[i][s] = sumcount[i-1][s-num]
            for s in range(0, 2*totalsum+1-num):
                sumcount[i][s] += sumcount[i-1][s+num]
        return sumcount[-1][offset + target]
        