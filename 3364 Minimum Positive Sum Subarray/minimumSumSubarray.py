from typing import List
import sys

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        i, j = 0, 0
        result = sys.maxsize
        for i in range(n):
            for k in range(l, r+1):
                if i + k < n + 1:
                    j = i + k
                    ls = sum(nums[i:j])
                    if ls > 0 and ls < result:
                        result = ls
        if result == sys.maxsize:
            result = -1
        return result

sol = Solution()
print(sol.minimumSumSubarray([3, -2, 1, 4], 2, 3))
print(sol.minimumSumSubarray([-2, 2, -3, 1], 2, 3))
print(sol.minimumSumSubarray([1, 2, 3, 4], 2, 4))