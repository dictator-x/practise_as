"""
1326. Minimum Number of Taps to Open to Water a Garden
"""
from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        nums = [0] * len(ranges)
        for i in range(len(ranges)):
            idx = max(0, i - ranges[i])
            nums[idx] = i+ranges[i]

        steps = 0
        l = 0
        e = 0

        for i in range(len(nums)):
            if i > e: return -1;
            if i > l:
                steps += 1
                l = e
            e = max(e, nums[i])
        return steps
