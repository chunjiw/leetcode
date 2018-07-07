# 159. Longest Substring with At Most Two Distinct Characters
# DescriptionHintsSubmissionsDiscussSolution
# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

# Example 1:

# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# Example 2:

# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        result = 0
        i, j = 0, 0
        letter = set()
        while j < len(s):
            if len(letter) < 2:
                letter.add(s[j])
                j += 1
                result = max(result, j - i)
            else: # when len(letter) == 2
                if s[j] in letter:
                    j += 1
                    result = max(result, j - i)
                else:
                    i = j - 2
                    while s[i] == s[j - 1]:
                        i -= 1
                    i += 1
                    letter = set([s[i], s[j]])
                    j += 1
        return result
