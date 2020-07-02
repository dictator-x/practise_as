"""
636. Exclusive Time of Functions
"""

from typing import List

# hint: this is time block
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ret = [0] * n
        tmp = []
        for log in logs:
            s = log.split(":")
            tmp.append((int(s[0]), s[1], int(s[2])))
        stack = []
        # Key variable.
        pre = 0
        for log in tmp:
            if log[1] == "start":
                if stack:
                    ret[stack[-1][0]] += log[2] - pre
                stack.append(log)
                pre = log[2]
            else:
                l = stack.pop()
                ret[l[0]] += log[2] - pre + 1
                # It is time block
                pre = log[2] + 1
        return ret
