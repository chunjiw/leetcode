# 153. Find Minimum in Rotated Sorted Array
# DescriptionHintsSubmissionsDiscussSolution
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2] 
# Output: 1
# Example 2:

# Input: [4,5,6,7,0,1,2]
# Output: 0


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return nums
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        
        while left < right - 1:
            mid = (left + right) / 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid
        
        if left < len(nums) - 1 and nums[left] > nums[left + 1]:
            return nums[left + 1]
        if right < len(nums) - 1 and nums[right] > nums[right + 1]:
            return nums[right + 1]
        return None
