"""
1383. Maximum Performance of a Team
"""

from typing import List
from heapq import heappop, heappush

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        s_e = []
        for i in range(n):
            s_e.append((efficiency[i], speed[i]))

        s_e.sort(key = lambda x:(-x[0]))
        ret = 0
        sums = 0
        heap = []

        for idx, val in enumerate(s_e):
            eff, spe = val
            if idx >= k:
                sums -= heappop(heap)
            sums += spe
            heappush(heap, spe)
            ret = max(ret, sums*eff)

        return ret % mod
