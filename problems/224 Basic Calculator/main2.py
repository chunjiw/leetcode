class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        curr_sign = 1
        global_sign = [1]
        curr_num = 0
        curr_sum = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                curr_num *= 10
                curr_num += int(s[i])
                i += 1
                continue
            curr_sum += curr_num * curr_sign * global_sign[-1]
            curr_num = 0
            curr_sign = 1
            if s[i:i+2] == '+(':
                global_sign.append(global_sign[-1])
                i += 2
            elif s[i:i+2] == '-(':
                global_sign.append(-1 * global_sign[-1])
                i += 2
            elif s[i] == ')':
                global_sign.pop()
                i += 1
            elif s[i] == '(':
                global_sign.append(global_sign[-1])
                i += 1
            elif s[i] == '+':
                i += 1
            elif s[i] == '-':
                curr_sign *= -1
                i += 1
        curr_sum += curr_num * curr_sign * global_sign[-1]
        return curr_sum

sol = Solution()
print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))
print(sol.calculate("(1+(4+5+2)-3)"))
print(sol.calculate("-(6+8)"))
print(sol.calculate("-(1+(4+5+2)-3)-(6+8)"))
