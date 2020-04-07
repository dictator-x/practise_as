"""
224. Basic Calculator
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ret = 0
        sign = 1
        operand = 0

        for char in s:
            if char.isdigit():
                operand = operand*10 + int(char)
            elif char == "+":
                ret += sign * operand
                sign = 1
                operand = 0
            elif char == "-":
                ret += sign * operand
                sign = -1
                operand = 0
            elif char == "(":
                stack.append(ret)
                stack.append(sign)

                ret = 0
                sign = 1
                operand = 0
            elif char == ")":
                ret += sign * operand
                ret = stack.pop() * ret
                ret += stack.pop()
                operand = 0
        return ret + sign * operand
