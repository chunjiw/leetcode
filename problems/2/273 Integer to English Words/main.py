from collections import deque

class Solution:

    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        d = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        result = deque()

        groups = ['', 'Thousand', 'Million', 'Billion']
        for g in groups:
            res = []
            m = num % 1000
            num //= 1000
            if m == 0:
                continue
            if m > 99:
                res.append(d[m // 100])
                res.append('Hundred')
            m %= 100
            if 0 < m <= 19:
                res.append(d[m])
            elif m > 19:
                res.append(d[m - m % 10])
                if m % 10 > 0:
                    res.append(d[m % 10])
            if g:
                res.append(g)
            result.appendleft(' '.join(res))
        return ' '.join(result)
    
sol = Solution()
print('#' + sol.numberToWords(1000000) + '#')
print('#' + sol.numberToWords(1000) + '#')
print('#' + sol.numberToWords(12345) + '#')
print('#' + sol.numberToWords(1234567) + '#')
print('#' + sol.numberToWords(1234567891) + '#')