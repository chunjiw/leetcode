class Solution:

    def grow(self, nums, k):
        if k == len(nums):
            return
        self.result.extend([a ^ nums[k] for a in self.result])
        self.grow(nums, k + 1)

    def subsetXORSum(self, nums: List[int]) -> int:
        self.result = [0]
        self.grow(nums, 0)
        return sum(self.result)