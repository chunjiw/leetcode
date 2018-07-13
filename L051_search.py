# 81. Search in Rotated Sorted Array II
# DescriptionHintsSubmissionsDiscussSolution
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# Follow up:

# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?




class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        if nums[0] == target or nums[-1] == target:
            return True
        
        left, right = 0, len(nums) - 1
        # make sure head and tail are different from
        if nums[0] == nums[-1]:
            tie = nums[0]
            while left < len(nums) and nums[left] == tie:
                left += 1
            while right >= 0 and nums[right] == tie:
                right -= 1
        
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return True
            if target > nums[0]: # target at first half
                if target < nums[mid] or nums[mid] <= nums[-1]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:   # target at second half
                if nums[mid] < target or nums[mid] >= nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1    
        return False
        
