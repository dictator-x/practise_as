# 8. String to Integer (atoi)

from typing import List

class Solution:
    def myAtoi(self, s: str) -> int:
        stripS = s.strip()
        sign = 1
        ret = 0

        if stripS == "":
            return 0

        if stripS[0] == "-":
            sign = -1
            stripS = stripS[1:]
        elif stripS[0] == "+":
            stripS = stripS[1:]

        for c in stripS:
            if self.isDigit(c) != True:
                break
            else:
                ret = ret * 10 + self.toDigit(c)
        ret = ret * sign

        if ret >= 2**31 -1:
            return 2**31 - 1
        elif ret <= -(2**31):
            return -(2**31)
        else:
            return ret

    def isDigit(self, char: str) -> bool:
        zero = ord('0')
        nine = ord('9')
        c = ord(char)
        if c >= zero and c <= nine:
            return True
        else:
            return False

    def toDigit(self, char: str) -> int:
        return ord(char) - ord('0')

if __name__ == "__main__":
    solution = Solution()
    print (solution.myAtoi("   -42"))
