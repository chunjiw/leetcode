# 239. Sliding Window Maximum
# DescriptionHintsSubmissionsDiscussSolution
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

# Example:

# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

# Follow up:
# Could you solve it in linear time?

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        if not nums:
            return []
        
        result = []
        dp = collections.deque()
        for i in range(k):
            while dp and nums[i] > nums[dp[-1]]:
                dp.pop()            
            dp.append(i)
            
        for i in range(k, len(nums)):
            result.append(nums[dp[0]])
            if i - dp[0] + 1 > k:
                dp.popleft()
            while dp and nums[i] > nums[dp[-1]]:
                dp.pop()
            dp.append(i)
                
        result.append(nums[dp[0]])
        return result
            
