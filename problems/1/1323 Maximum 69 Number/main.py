class Solution:

    def better(self, num: int) -> int:
        s = list(str(num))
        if '6' not in s:
            return num
        i = s.index('6')
        s[i] = '9'
        return int(''.join(s))

    def maximum69Number(self, num: int) -> int:
        changed = False
        result = []
        for d in str(num):
            if changed:
                result.append(d)
                continue
            if d == '6':
                changed = True
            result.append('9')
        return int(''.join(result))

sol = Solution()
print(sol.better(9669))