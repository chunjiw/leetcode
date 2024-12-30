class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        result = curr = nums[0]
        for num in nums[1:]:
            curr = num + max(curr, 0)
            result = max(result, curr)
        rightsum = nums.copy()
        rightmax = nums.copy()
        for i in range(n-2, -1, -1):
            rightsum[i] += rightsum[i+1]
            rightmax[i] = max(rightsum[i], rightmax[i+1])
        leftsum = 0
        for i, num in enumerate(nums):
            result = max(result, leftsum + rightmax[i])
            leftsum += num
        return result
        