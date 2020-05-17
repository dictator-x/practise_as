"""
862. Shortest Subarray with Sum at Least K
"""

from typing import List
import sys

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        ret = len(A) + 1

        pre_sum = [0]
        for i in A:
            pre_sum.append(pre_sum[-1] + i)

        monoq = []
        for idx, val in enumerate(pre_sum):
            while monoq and val <= pre_sum[monoq[-1]]:
                monoq.pop()
            while monoq and val - pre_sum[monoq[0]] >= K:
                print(pre_sum[monoq[0]])
                ret = min(ret, idx - monoq.pop(0))
            monoq.append(idx)

        return ret if ret < len(A) + 1 else -1
