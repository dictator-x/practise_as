"""
20. Valid Parentheses
"""
from sets import Set

class Solution:
    def isValid(self, s: str) -> bool:
        left_tokens = ("(", "[", "{")
        right_pair = {"]": "[", "}": "{", ")": "("}
        stack = []

        for i in range(len(s)):
            if s[i] in left_tokens:
                stack.append(s[i])
            else:
                if len(stack) == 0 or stack[-1] != right_pair[s[i]]:
                    return False
                else:
                    stack.pop()

        if len(stack) != 0:
            return False
        return True
