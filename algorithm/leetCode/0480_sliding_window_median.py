"""
480. Sliding Window Median
"""

from typing import List
import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = []
        ret = []

        for i in range(len(nums)):
            if i >= k:
                window.pop(bisect.bisect_left(window, nums[i-k]))

            bisect.insort_left(window, nums[i])

            if i >= k-1:
                median = (window[k//2] + window[k//2 - 1]) / 2 if k % 2 == 0 else window[k//2]
                ret.append(median)

        return ret
