# 161. One Edit Distance
# DescriptionHintsSubmissionsDiscussSolution
# Given two strings s and t, determine if they are both one edit distance apart.

# Note: 

# There are 3 possiblities to satisify one edit distance apart:

# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
# Example 1:

# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# Example 2:

# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
# Example 3:

# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """ 
        i = 0
        while i < min(len(s), len(t)) and s[i] == t[i]:
            i += 1
        if s[i:] == t[i:]:
            return False
        return s[i:] == t[i+1:] or s[i+1:] == t[i:] or s[i+1:] == t[i+1:]       
