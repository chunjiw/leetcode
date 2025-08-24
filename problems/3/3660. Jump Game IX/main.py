class Solution:
    def maxValue(self, nums: list[int]) -> list[int]:

        ans = nums.copy()
        n = len(nums)

        premax = [nums[0]] * n
        for i in range(1, n):
            premax[i] = max(premax[i-1], nums[i])

        sufmin = [nums[-1]] * n
        for i in range(n-2, -1, -1):
            sufmin[i] = min(sufmin[i+1], nums[i])

        a = 0
        for i in range(n):
            if i == n-1 or premax[i] <= sufmin[i+1]:
                for k in range(a, i+1):
                    ans[k] = premax[i]
                a = i+1
        
        return ans