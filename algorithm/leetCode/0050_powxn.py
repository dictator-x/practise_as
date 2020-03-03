"""
50. Pow(x, n)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        ret = 1
        acc = x

        while n != 0:
            if n % 2 == 1:
                ret *= acc

            acc *= acc
            n = n//2

        return ret
