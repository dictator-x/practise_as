"""
42. Trapping Rain Water
"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        ret = 0;
        n = len(height)
        if n < 3:
            return ret

        l, r = 0, n-1
        l_max, r_max = height[l], height[r]

        while l < r:
            if l_max < r_max:
                ret += l_max - height[l]
                l += 1
                # pre assgin the next height to prevent l_max - height[l] < 0
                l_max = max(height[l], l_max)
            else:
                ret += r_max - height[r]
                r -= 1
                r_max = max(height[r], r_max)
        return ret;
