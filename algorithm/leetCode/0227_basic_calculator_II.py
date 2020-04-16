"""
227. Basic Calculator II
"""
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = "+"
        number = 0

        i = 0

        while i < len(s):
            c = s[i]

            if c.isdigit():
                number = number*10 + int(c)

            if c == "(":
                # number == ?
                pass

            if c != " " and not c.isdigit() or i == len(s) - 1:
                if sign == "+":
                    stack.append(number)
                elif sign == "-":
                    stack.append(-number)
                elif sign == "*":
                    stack.append(stack.pop()*number)
                elif sign == "/":
                    stack.append(int(stack.pop()/number))
                sign = c
                number = 0
            i += 1

        ret = 0
        while len(stack) != 0:
            ret += stack.pop()
        return ret
