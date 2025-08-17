class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        m = max(nums)
        count = 0
        result = 1
        for num in nums:
            if num == m:
                count += 1
                result = max(result, count)
            else:
                count = 0
        return result