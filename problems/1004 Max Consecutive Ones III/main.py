from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i, j = 0, 0    # longest ones appear in nums[i:j]
        result = 0
        maxk = k
        while j < n:
            while j < n:
                if nums[j] == 0:
                    if k > 0:
                        k -= 1
                    else:
                        break
                j += 1
            result = max(result, j - i)
            while i < j and k == 0:
                if nums[i] == 0:
                    if k < maxk:
                        k += 1
                    else:
                        break
                i += 1
            if i == j and maxk == 0:
                i += 1
                j += 1
        return result

sol = Solution()
# print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
# print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
# print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 0))
print(sol.longestOnes([0,0,1,1], 1))


