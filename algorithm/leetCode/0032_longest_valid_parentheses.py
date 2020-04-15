"""
32. Longest Valid Parentheses
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ret = 0

        for i in range(len(s)):
            char = s[i]
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    # i is the position of nearest valid
                    stack.append(i)
                else:
                    ret = max(ret, i - stack[-1])
        return ret
