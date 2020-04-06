"""
829. Consecutive Numbers Sum
"""
import math

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ret = 0

        for m in range(1, int(math.sqrt(2*N)+1)):
            if (2*N - m**2 + m) % (2*m) == 0 and (2*N - m**2 + m) > 0:
                ret += 1

        return ret



