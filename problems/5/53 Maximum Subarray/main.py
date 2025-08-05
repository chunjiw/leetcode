class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = result = nums[0]
        for n in nums[1:]:
            curr = n + max(curr, 0)
            result = max(result, curr)
        return result