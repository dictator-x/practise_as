"""
354. Russian Doll Envelopes
"""

from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        l_e = sorted(envelopes, key=lambda x:(x[0], -x[1]))
        l_e = [ x[1] for x in l_e ]
        dp = []

        for i in range(len(l_e)):
            idx = bisect.bisect_left(dp, l_e[i])
            if idx == len(dp):
                dp.append(l_e[i])
            else:
                dp[idx] = l_e[i]

        return len(dp)


