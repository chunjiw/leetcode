# 15. 3Sum
# DescriptionHintsSubmissionsDiscussSolution
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            pairs = self.twoSum(nums, i, -nums[i])
            for pair in pairs:
                self.add(result, pair + [nums[i]])
        return result

    def twoSum(self, nums, start, target):
        left, right = start + 1, len(nums) - 1
        result = []
        while left < right:
            if nums[left] + nums[right] == target:
                result.append([nums[left], nums[right]])
                left += 1
                right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return result

    def add(self, result, triplet):
        triplet.sort()
        for tri in result:
            if tri == triplet:
                return
        result.append(triplet)
