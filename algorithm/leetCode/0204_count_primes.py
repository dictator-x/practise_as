"""
204. Count Primes
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1: return 0
        list = [True] * (n+1)

        list[0] = False
        list[1] = False

        for i in range(2, n+2):
            for j in range(i+i, n, i):
                list[j] = False
        return list[:-1].count(True)

