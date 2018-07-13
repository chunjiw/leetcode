# 33. Search in Rotated Sorted Array
# DescriptionHintsSubmissionsDiscussSolution
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        
        # assume target > nums[0]
        if target > nums[0]:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) / 2
                if nums[mid] == target:
                    return mid
                if target < nums[mid] or nums[mid] < nums[0]:
                    right = mid - 1
                else:
                    left = mid + 1   
        elif target < nums[-1]:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) / 2
                if nums[mid] == target:
                    return mid
                if target > nums[mid] or nums[mid] > nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
