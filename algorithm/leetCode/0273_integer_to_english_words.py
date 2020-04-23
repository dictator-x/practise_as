"""
273. Integer to English Words
"""
from enum import Enum

class HundredPlus(Enum):
  #those also work though not required
  #and more could be added as well
  #Quadrillion = 10**15
  #Trillion = 10**12
  Billion = 10**9
  Million = 10**6
  Thousand = 1000
  Hundred = 100

class TwentyPlus(Enum):
  Ninety = 90
  Eighty = 80
  Seventy = 70
  Sixty = 60
  Fifty = 50
  Forty = 40
  Thirty = 30
  Twenty = 20

class NineteenMinus(Enum):
  Nineteen = 19
  Eighteen = 18
  Seventeen = 17
  Sixteen = 16
  Fifteen = 15
  Fourteen = 14
  Thirteen = 13
  Twelve = 12
  Eleven = 11
  Ten = 10
  Nine = 9
  Eight = 8
  Seven = 7
  Six = 6
  Five = 5
  Four = 4
  Three = 3
  Two = 2
  One = 1

class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"

        billion = 10**9
        million = 10**6
        thousand = 10**3
        hundred = 10**2

        def lessThousand(num):
            ret = []
            if num // hundred > 0:
                ret.append(NineteenMinus(num // hundred).name)
                ret.append(HundredPlus(hundred).name)

            num = num % hundred

            if num >= 20:
                ret.append(TwentyPlus(num - num % 10).name)
                num = num % 10
                if num > 0:
                    ret.append(NineteenMinus(num).name)

            elif num < 20 and num > 0:
                ret.append(NineteenMinus(num).name)

            return ret

        ret = []

        p = lessThousand(num // billion)
        if len(p) > 0:
            ret = ret + p + [HundredPlus(billion).name]
        num = num - (num // billion) * billion

        p = lessThousand(num // million)
        if len(p) > 0:
            ret = ret + p + [HundredPlus(million).name]
        num = num - (num // million) * million

        p = lessThousand(num // thousand)
        if len(p) > 0:
            ret = ret + p + [HundredPlus(thousand).name]
        num = num - (num // thousand) * thousand

        if num > 0:
            ret = ret + lessThousand(num)

        return " ".join(ret)

if __name__ == "__main__":
    print(NineteenMinus(19).name)
    solution = Solution()
    print(solution.numberToWords(1234567))
