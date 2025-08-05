class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        if dividend == divisor:
            return 1
        if dividend == -2**31:
            if divisor == -1:
                return 2**31 - 1
            elif divisor > 1:
                return -1 + self.divide(dividend + divisor, divisor)
            else:   # divisor < -1
                return 1 + self.divide(dividend - divisor, divisor)
        if dividend < 0 and divisor < 0:
            return self.divide(-dividend, -divisor)
        if dividend < 0 or divisor < 0:
            return -self.divide(abs(dividend), abs(divisor))
        if dividend < divisor:
            return 0
        quotient = 0
        factor = 1
        chunk = divisor
        while dividend >= chunk:
            dividend -= chunk
            quotient += factor
            chunk += chunk
            factor += factor
        return quotient + self.divide(dividend, divisor)