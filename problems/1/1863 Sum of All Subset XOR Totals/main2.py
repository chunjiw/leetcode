class Solution:

    def grow(self, nums, k, curr):
        if k == len(nums):
            self.result += curr
            return
        self.grow(nums, k+1, curr)
        self.grow(nums, k+1, curr^nums[k])

    def subsetXORSum(self, nums: List[int]) -> int:
        self.result = 0
        self.grow(nums, 0, 0)
        return self.result