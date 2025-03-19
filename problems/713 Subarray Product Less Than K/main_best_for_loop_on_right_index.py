from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        n = len(nums)
        result = 0
        prod = 1
        i = 0
        for j in range(n):
            prod *= nums[j]
            # here, prod is [i,j] inclusive
            while prod >= k:
                prod //= nums[i]
                i += 1
            result += j - i + 1
        return result

sol = Solution()
print(sol.numSubarrayProductLessThanK([57,44,92,28,66,60,37,33,52,38,29,76,8,75,22], 18))