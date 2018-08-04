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
        
        result = len(nums) + 1
        ssum = 0
        fast = 0
        
        for slow in range(len(nums)):
            while ssum < s and fast < len(nums):
                ssum += nums[fast]
                fast += 1
            if ssum >= s:
                result = min(result, fast - slow)
            ssum -= nums[slow]
        
        if result > len(nums):
            return 0
        return result
        
                
            
