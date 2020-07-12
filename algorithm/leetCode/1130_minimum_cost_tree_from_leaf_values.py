"""
1130. Minimum Cost Tree From Leaf Values
"""

from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        max_val = 10 ** 9
        stack = [max_val]
        ret = 0

        for val in arr:
            while val > stack[-1]:
                md = stack.pop()
                ret += md*min(stack[-1], val)
            stack.append(val)

        stack.pop(0)
        while len(stack)>1:
            ret += stack.pop() * stack[-1]
        return ret
