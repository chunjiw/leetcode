from typing import List

# at end of while loop, nums[i:j] excluding nums[j] is current valid window

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        n = len(nums)
        j = 0
        prod = 1
        result = 0
        for i in range(n):
            while j < n and prod * nums[j] < k:
                prod *= nums[j]
                j += 1
                # add all subarrays of nums[i:j] that includes nums[j-1]
                result += j - i
            # remove nums[i] from product only if i is included in the window
            if i < j:
                prod //= nums[i]
            else:
                j += 1
        return result

sol = Solution()
print(sol.numSubarrayProductLessThanK([57,44,92,28,66,60,37,33,52,38,29,76,8,75,22], 18))