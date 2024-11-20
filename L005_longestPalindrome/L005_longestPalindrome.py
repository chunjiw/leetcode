# 5. Longest Palindromic Substring
# DescriptionHintsSubmissionsDiscussSolution
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        maxlen = 1
        result = s[0]
        for i in range(len(s)):
            j = 1
            while 0 <= i - j and i + j < len(s) and s[i - j] == s[i + j]:
                j += 1
            if maxlen < j * 2 - 1:
                maxlen = j * 2 - 1
                result = s[i - j + 1: i + j]
            j = 1
            while 0 <= i - j and i + j - 1 < len(s) and s[i - j] == s[i + j - 1]:
                j += 1
            if maxlen < j * 2 - 2:
                maxlen = j * 2 - 2
                result = s[i - j + 1: i + j - 1]
        return result
