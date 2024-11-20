# 718. Maximum Length of Repeated Subarray
# DescriptionHintsSubmissionsDiscussSolution
# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

# Example 1:
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
# Note:
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        result = 0
        dp = [0 for _ in range(len(A) + 1)]
        ndp = [0 for _ in range(len(A) + 1)]
        for i in range(len(B)):
            for j in range(len(A)):
                if A[j] == B[i]:
                    ndp[j + 1] = dp[j] + 1
                    result = max(result, ndp[j + 1])
                else:
                    ndp[j + 1] = 0            
            dp, ndp = ndp, dp
        return result
