# 525. Contiguous Array
# DescriptionHintsSubmissionsDiscussSolution
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.



from collections import defaultdict

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP: first, dp1 and dp0 represents how many 1s and 0s before index i
        # then ddp = dp1 - dp0
        # when there are same values, that means dp1[j] - dp1[i] = dp0[j] - dp0[i], such that
        # there are same number of 1s and 0s between j and i.
        # Or, simply construct ddp: ddp[i] is the difference between number of 1s and 0s before index i 
                
        dp = [0 for _ in range(len(nums) + 1)]
        index = defaultdict(int)
        for i, num in enumerate(nums):
            dp[i + 1] = dp[i] + num*2 - 1
            index[dp[i + 1]] = max(index[dp[i + 1]], i + 1)
            
        result = 0
        
        for i, cnt in enumerate(dp):
            result = max(result, index[cnt] - i)
        
        return result
