from typing import List
import sys

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        cumsum = 0
        n = len(nums)
        for i in range(n):
            nums[i] += cumsum
            cumsum = nums[i]
        nums.insert(0, 0)
        result = sys.maxsize
        for i in range(n):
            for size in range(l, r+1):
                if i + size < n + 1:
                    s = nums[i + size] - nums[i]
                    print(i, size, s)
                    if s > 0 and s < result:
                        result = s
        if result == sys.maxsize:
            result = -1
        return result

sol = Solution()
# print(sol.minimumSumSubarray([3, -2, 1, 4], 2, 3))
# print(sol.minimumSumSubarray([-2, 2, -3, 1], 2, 3))
print(sol.minimumSumSubarray([1, 2, 3, 4], 2, 4))