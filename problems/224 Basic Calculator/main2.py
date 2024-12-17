class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = [1]     # keep track of sign of this parenthesis
        num, sign = 0, 1
        result = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num *= 10
                num += int(s[i])
                i += 1
                continue
            result += num * sign * stack[-1]
            num, sign = 0, 1
            if s[i:i+2] == '+(':
                stack.append(stack[-1])
                i += 1
            elif s[i:i+2] == '-(':
                stack.append(-1 * stack[-1])
                i += 1
            elif s[i] == ')':
                stack.pop()
            elif s[i] == '(':
                stack.append(stack[-1])
            elif s[i] == '-':
                sign *= -1
            i += 1
        result += num * sign * stack[-1]
        return result

sol = Solution()
print(sol.calculate("(9)"))
# print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))
# print(sol.calculate("(1+(4+5+2)-3)"))
# print(sol.calculate("-(6+8)"))
# print(sol.calculate("-(1+(4+5+2)-3)-(6+8)"))
