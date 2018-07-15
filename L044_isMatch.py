# 44. Wildcard Matching
# DescriptionHintsSubmissionsDiscussSolution
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:

# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:

# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:

# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        if not s:
            return all([c == '*' for c in p])
        
        match = [[None for j in range(len(s) + 1)] for i in range(len(p) + 1)]
        
        match[0][0] = True
        for j in range(len(s)):
            match[0][j + 1] = False
        for i in range(len(p)):
            match[i + 1][0] = match[i][0] and p[i] == '*'
                 
        for i in range(0, len(p)):
            for j in range(0, len(s)):
                match[i + 1][j + 1] = \
                    ((p[i] == s[j] or p[i] == '?') and match[i][j]) or \
                    (p[i] == '*' and (match[i + 1][j] or match[i][j + 1]))
                   
        return match[-1][-1]        
            
        
        
       
