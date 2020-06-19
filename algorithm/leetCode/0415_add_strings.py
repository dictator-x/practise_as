"""
415. Add Strings
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n_num1 = len(num1)
        n_num2 = len(num2)

        if n_num1 < n_num2:
            num1 = "0"*(n_num2-n_num1)+num1
        elif n_num1 > n_num2:
            num2 = "0"*(n_num1-n_num2)+num2

        print(num1, num2)
        ret = ""
        carry = 0

        for i in range(len(num1)-1, -1, -1):
            cur = int(num1[i])+int(num2[i]) + carry
            carry = 1 if cur > 9 else 0
            ret = str(cur%10) + ret

        return str(carry) + ret if carry else ret
