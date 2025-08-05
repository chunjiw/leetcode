class Solution:

    def cal(self, x, zero, one, mem):
        modulo = 1000000007
        if x == 0:
            return 1
        if x < zero and x < one:
            return 0
        if x == zero == one:
            return 2
        if min(zero, one) == x:
            return 1
        if x in mem:
            return mem[x]
        y = self.cal(x - zero, zero, one, mem) + self.cal(x - one, zero, one, mem)
        mem[x] = y % modulo
        return y

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mem = dict()
        result = 0
        modulo = 1000000007
        for x in range(low, high+1):
            result = (result + self.cal(x, zero, one, mem)) % modulo
        return result
