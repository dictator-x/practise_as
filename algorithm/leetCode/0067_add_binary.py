"""
67. Add Binary
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n_a = len(a)
        n_b = len(b)
        if n_a < n_b:
            a = "0"*(n_b-n_a) + a
        elif n_b < n_a:
            b = "0"*(n_a-n_b) + b

        carry = 0
        ret = ""

        r_a = a[::-1]
        r_b = b[::-1]

        for i in range(0, len(r_a)):
            d = int(r_a[i]) + int(r_b[i]) + carry
            carry = 1 if d >= 2 else 0
            ret = str(d%2) + ret

        if carry == 1: ret = "1"+ ret
        return ret
