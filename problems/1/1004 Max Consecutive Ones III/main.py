from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0    # substring of ones is nums[i:j]. After for loop exit, j is effectively len(nums)
        for j in range(len(nums)):
            if nums[j] == 0:
                k -= 1
            # only move i when we flipped too many zeros
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
        return len(nums) - i

sol = Solution()
print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 0))
print(sol.longestOnes([0,0,1,1], 1))
