"""
394. Decode String
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        factor = 0
        sub = ""

        for c in s:
            if c.isdigit():
                factor = factor * 10 + int(c)
            elif c == "[":
                stack.append((factor, sub))
                factor = 0
                sub = ""
            elif c == "]":
                factor, pre = stack.pop()
                sub = pre + sub*factor
                factor = 0
            else:
                sub += c
        return sub
