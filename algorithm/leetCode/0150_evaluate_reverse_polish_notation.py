"""
150. Evaluate Reverse Polish Notation
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t.isdigit() or t[0] == "-" and t[1:].isdigit():
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    tmp = a + b
                elif t == "-":
                    tmp = a - b
                elif t == "*":
                    tmp = a * b
                elif t == "/":
                    tmp = int(a / b)

                stack.append(tmp)

        return stack[-1]
