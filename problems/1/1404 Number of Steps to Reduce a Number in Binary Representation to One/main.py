class Solution:
    def numSteps(self, s: str) -> int:
        stack = [int(d) for d in s]
        steps = 0
        carry = 0
        while len(stack) > 1 :
            if (not carry and stack[-1] == 0) or (carry and stack[-1] == 1):
                stack.pop()
                steps += 1
            else: #(not carry and stack[-1] == 1) or (carry and stack[-1] == 0):
                stack.pop()
                carry = 1
                steps += 2
        return steps + carry 
        