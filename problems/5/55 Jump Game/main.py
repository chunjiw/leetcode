class Solution:
    def canJump(self, nums: list[int]) -> bool:
        remain = nums[0]
        for i in range(1, len(nums)):
            if remain == 0:
                return False
            remain = max(remain - 1, nums[i])
        return True

#  23114
#  23214
# 32104
# 3210