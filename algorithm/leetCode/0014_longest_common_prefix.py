"""
14. Longest Common Prefix
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""

        ret = strs[0]

        for s in strs[1:]:
            tmp = ""
            # i = 0
            # while i < len(ret) and i < len(s) and ret[i] == s[i]:
            #     tmp += ret[i]
            #     i += 1
            while not s.startswith(ret):
                ret = ret[:-1]

        return ret
