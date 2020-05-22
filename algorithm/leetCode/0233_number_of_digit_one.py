"""
233. Number of Digit One
"""

class Solution:
    def countDigitOne(self, n: int) -> int:
        ret = 0
        i = 1
        while i <= n:
            divider = i * 10
            print(n//divider, i)
            print(n % divider - i + 1)
            ret += (n//divider)*i + min(max(n % divider - i + 1, 0), i)
            i *= 10

        return ret
