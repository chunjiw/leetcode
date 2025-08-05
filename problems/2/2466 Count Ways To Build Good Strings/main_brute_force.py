class Solution:

    def build(self, low, high, a, b, curr):
        if low <= curr <= high:
            self.result += 1
        if curr > high:
            return
        self.build(low, high, a, b, curr + a)
        self.build(low, high, a, b, curr + b)

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.result = 0
        self.build(low, high, zero, one, 0)
        return self.result