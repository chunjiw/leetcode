from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        n = len(nums)
        j = 0
        prod = 1
        zeros = 0
        result = 0
        for i in range(n):
            while j < n and (prod * nums[j] < k or zeros > 0):
                if nums[j]:
                    prod *= nums[j]
                else:
                    zeros += 1
                j += 1
                # add all subarrays of nums[i:j] that includes nums[j-1]
                result += j - i
            # remove nums[i] from product only if i is included in the window
            if i < j:
                if nums[i]:
                    prod //= nums[i]
                else:
                    zeros -= 1
            else:
                j += 1
        return result

sol = Solution()
print(sol.numSubarrayProductLessThanK([57,44,92,28,66,60,37,33,52,38,29,76,8,75,22], 18))