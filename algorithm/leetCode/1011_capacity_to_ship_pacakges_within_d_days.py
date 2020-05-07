"""
1011. Capacity To Ship Packages Within D Days
"""
from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        w_sum = 0
        w_max = 0
        for w in weights:
            w_sum += w
            if w > w_max:
                w_max = w

        def canDivide(m):
            count = 1
            d_sum = 0
            for w in weights:
                if w + d_sum > m:
                    count += 1
                    d_sum = 0
                    if count > D: return False
                d_sum += w

            return True

        # optimal result is between w_max and w_sum
        lo, hi, m = w_max, w_sum, 0
        # do the binary guess.
        # can not equal otherwist will go into info looping.
        while lo < hi:
            m = lo + (hi -lo ) // 2

            if canDivide(m):
                # m is too big.
                # so low hi
                hi = m
            else:
                # m is too small can not divide into D group
                lo = m+1

        return lo
