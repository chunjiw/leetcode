class Solution:

    def pm(self, nums, m, result):
        if m == len(nums) - 1:
            result.append(nums.copy())
        else:
            for i in range(m, len(nums)):
                nums[m], nums[i] = nums[i], nums[m]
                self.pm(nums, m + 1, result)
                nums[m], nums[i] = nums[i], nums[m]

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.pm(nums, 0, result)
        return result