"""
1249. Minimum Remove to Make Valid Parentheses
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left_idxs = set()
        right_idxs = set()
        pair = []

        for idx, c in enumerate(s):
            if c == "(":
                pair.append(idx)
                left_idxs.add(idx)
            elif c == ")":
                if not pair:
                    right_idxs.add(idx)
                else:
                    left_idxs.remove(pair.pop())
        ret = ""
        for idx, c in enumerate(s):
            if idx in left_idxs or idx in right_idxs:
                continue
            ret += c

        return ret
