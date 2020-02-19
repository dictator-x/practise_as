# 65. Valid Number

class Solution:
    def isNumber(self, s: str) -> bool:
        stripS = s.strip()
        if stripS == "" or stripS == "." or stripS == "e":
            return False
        if stripS[0] == "-" or stripS[0] == "+":
            stripS = stripS[1:]

        seeE = False
        seePoint = False
        seeDigitBeforeE = False
        index = -1
        numberBeforeE = 0
        numberBeforeIsZero = True

        print(stripS)
        for c in stripS:
            index = index + 1
            if self.isDigit(c) == False and c != "." and c != "e":
                return False;
            elif c == "e":
                break
            elif c == ".":
                if seePoint == True:
                    return False;
                else:
                    seePoint = True
            else:
                seeDigitBeforeE = True
        print(index)
        if index == -1:
            return False
        if stripS[index] == ".":
            if seeDigitBeforeE:
                return True
            else:
                return False
        if index == len(stripS) - 1 and stripS[index] != "e":
            return True


        if seeDigitBeforeE == False:
            return False

        if stripS[index] != 'e':
            return False

        if stripS[index-1] == '-':
            return False

        stripS = stripS[index:]

        if len(stripS) <= 1:
            return False

        stripS = stripS[1:]

        if stripS[0] == "-" or stripS[0] == "+":
            stripS = stripS[1:]

        seeDigitAfterE = False
        for c in stripS:
            if self.isDigit(c) == False:
                return False
            else:
                seeDigitAfterE = True

        if seeDigitAfterE == False:
            return False

        return True

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
    print (solution.isNumber(""))

