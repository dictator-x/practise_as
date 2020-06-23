"""
202. Happy Number
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        def genNext(n):
            ret = 0
            while n:
                n, r = divmod(n, 10)
                ret += r**2
            return ret

        seen = set()
        # n in seen => loop
        while n != 1 and n not in seen:
            seen.add(n)
            n = genNext(n)

        return n == 1

