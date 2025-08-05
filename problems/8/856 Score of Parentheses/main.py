class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for p in s:
            if p == '(':
                stack.append(0)
            else:
                score = stack.pop()
                if score == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += score * 2
        return stack[0]
            