# 18. 4Sum
# DescriptionHintsSubmissionsDiscussSolution
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                pairs = self.twoSum(nums, j, target - nums[i] - nums[j])
                for pair in pairs:
                    self.add(result, pair + [nums[i], nums[j]])
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
    
    def add(self, result, candidate):
        candidate.sort()
        for quad in result:
            if quad == candidate:
                return
        result.append(candidate)
        