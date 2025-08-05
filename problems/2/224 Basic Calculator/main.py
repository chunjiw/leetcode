# Consider tokens as of these types: +(, -(, (, +d, -d, d, ).

class Solution:

    def getNumber(self, s, i):
        # should guarantee i is within range and s[i].isdigit()
        j = i + 1
        while j < len(s) and s[j].isdigit():
            j += 1
        return 'd', int(s[i:j]), j
        
    def getNext(self, s, i):
        if i >= len(s):
            return None, None, None
        if s[i].isdigit():
            return self.getNumber(s, i)
        if s[i] in ('(', ')'):
            return s[i], 1, i + 1
        # here, should guarantee s[i] is not the end
        if s[i] in ('+', '-') and s[i+1].isdigit():
            _, num, j = self.getNumber(s, i+1)
            if s[i] == '+':
                return 'd', num, j
            else:
                return 'd', -num, j
        if s[i] == '+' and s[i+1] == '(':
            return '(', 1, i + 2
        if s[i] == '-' and s[i+1] == '(':
            return '(', 0, i + 2
        print(f"Unknown operator {s[i]} at {i}")
        
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        i = 0
        while i < len(s):
            kind, value, i = self.getNext(s, i)
            if kind == 'd':
                if not stack or stack[-1][1] != 'd':
                    stack.append([value, 'd'])
                else:
                    stack[-1][0] += value
            elif kind == '(':
                stack.append([0, '+' if value else '-'])
            elif kind == ')':
                num, _ = stack.pop()
                _, op = stack.pop()
                value = num if op == '+' else -num
                if not stack or stack[-1][1] != 'd':
                    stack.append([value, 'd'])
                else:
                    stack[-1][0] += value
        return stack[0][0]

sol = Solution()
print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))
print(sol.calculate("-(6+8)"))



        