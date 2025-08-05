from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        sol = [nums[0], max(nums[:2])]
        for i in range(2, n):
            sol.append(max(nums[i] + sol[i-2], sol[i-1]))
        return sol[-1]

sol = Solution()
print(sol.rob([1,2,3,1]))