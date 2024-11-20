# 140. Word Break II
# DescriptionHintsSubmissionsDiscussSolution
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:

# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        dp = [True] + [False] * len(s)
        bag = set(wordDict)
        dp_sets = [[] for _ in range(len(s) + 1)]
        dp_sets[0].append([0])
        
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    for solution in dp_sets[j]:
                        dp_sets[i].append(solution + [i])
        result = []                
        for spaces in dp_sets[-1]:
            solution = ""
            for i in range(len(spaces) - 1):
                solution += ' ' + s[spaces[i]:spaces[i+1]]
            result.append(solution[1:])
        return result
                    
