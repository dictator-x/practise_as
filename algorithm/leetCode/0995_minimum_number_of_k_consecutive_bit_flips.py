"""
995. Minimum Number of K Consecutive Bit Flips
"""

from typing import List

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        event_end = [0] * len(A)
        ret = 0
        flip = 0

        for i, v in enumerate(A):
            # Reset event affectiveness.
            flip = flip ^ event_end[i]

            if ( flip ^ v ) == 0:
                # Do not have enough elements to flip
                if (i+K) > len(A): return -1

                ret += 1
                flip ^= 1
                # Set close event point.
                if (i+K) < len(A): event_end[i+K] = 1

        return ret

