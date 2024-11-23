class Solution:
    def makeRomanDigit(self, num, one, five, ten):
        if num == 0:
            return ''
        if 0 < num < 4:
            return ''.join([one] * num)
        if num == 4:
            return ''.join([one, five])
        if num == 5:
            return five
        if 5 < num < 9:
            return ''.join([five] + [one] * (num - 5))
        if num == 9:
            return ''.join([one, ten])

    def intToRoman(self, num: int) -> str:
        thousand = ''.join(['M'] * (num // 1000))
        hundred = self.makeRomanDigit((num % 1000) // 100, 'C', 'D', 'M')
        ten = self.makeRomanDigit((num % 100) // 10, 'X', 'L', 'C')
        one = self.makeRomanDigit(num % 10, 'I', 'V', 'X')
        return ''.join([thousand, hundred, ten, one])

sol = Solution()
print(sol.intToRoman(3749))
print(sol.intToRoman(58))
print(sol.intToRoman(1994))
