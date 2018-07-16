# 128. Longest Consecutive Sequence
# DescriptionHintsSubmissionsDiscussSolution
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n) complexity.

# Example:

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bag = set(nums)
        streak = 0
        longstreak = 0
        count = -1
        for num in nums:
            if num - 1 not in bag:
                count = num
                streak = 1
            while count + 1 in bag:
                count += 1
                streak += 1
            longstreak = max(longstreak, streak)
        return longstreak
