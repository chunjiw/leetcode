class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = [1]     # keep track of sign of this parenthesis
        num, sign = 0, 1
        result = 0
        for i, ch in enumerate(s):
            if ch.isdigit():
                num *= 10
                num += int(ch)
            elif i > 0 and s[i-1].isdigit():
                result += num * sign * stack[-1]
                num, sign = 0, 1
            if ch == '-':
                sign *= -1
            elif ch == '(':
                stack.append(sign * stack[-1])
                sign = 1
            elif ch == ')':
                stack.pop()
        result += num * sign * stack[-1]
        return result

sol = Solution()
print(sol.calculate("-(9)"))
print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))
print(sol.calculate("(1+(4+5+2)-3)"))
print(sol.calculate("-(6+8)"))
print(sol.calculate("-(1+(4+5+2)-3)-(6+8)"))
