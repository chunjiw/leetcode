from typing import List
import sys

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        result = sys.maxsize
        if l > n:
            return -1
        ss = sum(nums[:l-1])
        for k in range(l, r+1):
            ss += nums[k-1]
            for i in range(n - k + 1):
                if i == 0:
                    ls = ss
                else:
                    ls -= nums[i - 1]
                    ls += nums[i + k - 1]
                if ls > 0 and ls < result:
                    result = ls
        if result == sys.maxsize:
            result = -1
        return result

sol = Solution()
print(sol.minimumSumSubarray([3, -2, 1, 4], 2, 3))
print(sol.minimumSumSubarray([-2, 2, -3, 1], 2, 3))
print(sol.minimumSumSubarray([1, 2, 3, 4], 2, 4))
print(sol.minimumSumSubarray([7, 3], 2, 2))
print(sol.minimumSumSubarray([-3, 17], 1, 2))