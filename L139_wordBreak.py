# 139. Word Break
# DescriptionHintsSubmissionsDiscussSolution
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false



class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        bag = set(wordDict)
        memo = dict()
        return self.helper(s, bag, 0, memo)
    
    def helper(self, s, bag, start, memo):
        if start == len(s):
            return True
        if start in memo:
            return memo[start]
        for i in range(start + 1, len(s)+1):
            if s[start:i] in bag:
                if self.helper(s, bag, i, memo):
                    memo[start] = True
                    return True
        memo[start] = False
        return False
