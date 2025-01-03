class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        result = 0
        for n in nums[:-1]:
            if 2 * n >= nums[-1]:
                result += 1
        return result