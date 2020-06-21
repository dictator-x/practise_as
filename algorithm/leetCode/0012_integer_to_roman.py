"""
12. Integer to Roman
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        value = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }

        ret = ""
        s_num = str(num)

        for idx, c in enumerate(s_num[::-1]):
            if c == "0": continue
            factor = 10 ** idx
            d = int(c)
            if d == 1 or d == 5:
                ret = value[d*factor] + ret
            elif d == 4:
                ret = value[1*factor] + value[5*factor] + ret
            elif d == 9:
                ret = value[1*factor] + value[10*factor] + ret
            elif d < 4:
                ret = value[1*factor]*d + ret
            elif d < 9:
                ret = value[5*factor] + value[1*factor]*(d-5) + ret

        return ret
