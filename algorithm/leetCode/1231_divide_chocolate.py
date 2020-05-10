"""
1231. Divide Chocolate
"""
from typing import List
import sys

# find maximum of smallest part that is divid by K parts
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        # range of guess will between min(sweetness) and sum(sweetness)
        min_guess = sys.maxsize
        max_guess = 0
        for sweet in sweetness:
            max_guess += sweet
            min_guess = min(sweet, min_guess)

        def canDivide(md):
            sum_interval = 0
            count = 0
            for sweet in sweetness:
                sum_interval += sweet
                if sum_interval >= md:
                    sum_interval = 0
                    count += 1
            if count >= K+1:
                return True
            else:
                return False

        lo, hi, md = min_guess, max_guess, 0
        while lo < hi:
            md = lo + (hi - lo + 1) // 2
            if canDivide(md):
                # md is too small
                lo = md
            else:
                hi = md - 1

        return lo
