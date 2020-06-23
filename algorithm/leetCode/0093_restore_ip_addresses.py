"""
93. Restore IP Addresses
"""

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []

        def isValid(s):
            ip = int(s)
            if 0 <= ip <= 255:
                if ip != 0 and s[0] == "0": return False
                if ip == 0 and len(s) > 1: return False
                return True
            else:
                return False

        def dfs(remain, pres, cur):
            if cur > 3:
                if not remain:
                    ret.append(".".join(pres))
                else:
                    return

            for l in range(1, 4):
                if len(remain) >= l:
                    take = remain[0:l]
                    rest = remain[l:]

                    if isValid(take):
                        pres.append(take)
                        dfs(rest, pres, cur+1)
                        pres.pop()

        dfs(s, [], 0)
        return ret

