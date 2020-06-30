"""
528. Random Pick with Weight
"""

from typing import List
from random import random

class Solution:

    def __init__(self, w: List[int]):
        self.pre_sum = []
        self.total = 0
        for val in w:
            self.total += val
            self.pre_sum.append(self.total)

    def pickIndex(self) -> int:
        pick = self.total * random()

        lo, hi = 0, len(self.pre_sum)-1
        while lo < hi:
            md = lo + (hi - lo) // 2
            if pick <= self.pre_sum[md]:
                hi = md
            else:
                lo = md+1

        return lo
