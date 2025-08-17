# 209. Minimum Size Subarray Sum
# DescriptionHintsSubmissionsDiscussSolution
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        currsum = [0]
        for num in nums:
            currsum.append(currsum[-1] + num)
            
        result = len(nums) + 1
        
        for i, small in enumerate(currsum):
            # binary search for smallest big such that big - small >= s
            # or for smallist big such that big >= s + small
            left, right = i + 1, len(currsum) - 1
            while left < right:
                mid = (left + right) / 2
                if currsum[mid] < s + small:
                    left = mid + 1
                else:
                    right = mid
            if currsum[right] >= s + small:
                result = min(result, right - i)
        if result > len(nums):
            return 0
        return result
                
            
