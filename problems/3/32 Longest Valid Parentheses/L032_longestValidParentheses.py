# 32. Longest Valid Parentheses
# DescriptionHintsSubmissionsDiscussSolution
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
    
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        result = 0
        for i in range(len(s)):
            local = 0
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 1:
                    stack = [i]
                if len(stack) > 1:
                    stack.pop()
                    local = max(local, i - stack[-1])
            result = max(result, local)
        return result
                
