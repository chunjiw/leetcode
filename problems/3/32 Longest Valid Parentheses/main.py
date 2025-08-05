class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # if stack is emptied, immediately append, so it is almost never empty
        # stack[0] is one before the start of valid subarray
        stack = [-1]
        longest = 0
        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            else:
                stack.pop()
                # if empty, means subarray not valid; start fresh
                if not stack:
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])
        return longest