"""
739. Daily Temperatures
"""

from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(T)

        for i in range(len(T)-1, -1, -1):
            while stack and T[i] >= stack[-1][1]:
                stack.pop()

            if stack:
                ret[i] = stack[-1][0] - i
            stack.append((i, T[i]))
        return ret
