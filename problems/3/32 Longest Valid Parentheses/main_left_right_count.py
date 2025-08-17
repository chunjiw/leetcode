class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        for p in s:
            if p == '(':
                left += 1
            if p == ')':
                right += 1
            if left < right:
                left, right = 0, 0
            elif left == right:
                longest = max(longest, left + right)
        left, right = 0, 0
        for p in reversed(s):
            if p == '(':
                left += 1
            if p == ')':
                right += 1
            if left > right:
                left, right = 0, 0
            elif left == right:
                longest = max(longest, left + right)
        return longest