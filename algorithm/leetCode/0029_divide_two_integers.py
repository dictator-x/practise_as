"""
29. Divide Two Integers
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        sign = -1 if dividend < 0 and divisor > 0  or dividend > 0 and divisor < 0 else 1
        ret = 0

        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            i = 1
            temp = divisor

            while dividend >= (temp << 1):
                temp = temp << 1
                i = i << 1

            dividend = dividend - temp
            ret += i
        if sign < 0:
            ret = -ret
        return min(MAX_INT, max(MIN_INT, ret))
