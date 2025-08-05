class Solution:
    def __init__(self):
        self.happyset = set([1])

    def sumsquare(self, n):
        result = 0
        while n > 0:
            result += (n % 10) * (n % 10)
            n //= 10
        return result

    def isHappy(self, n):
        if n in self.happyset:
            return True
        seen = set([n])
        m = n
        while n != 1:
            n = self.sumsquare(n)
            if n == 1:
                self.happyset.add(m)
                return True
            elif n in seen:
                return False
            else:
                seen.add(n)
