"""
34. Find First and Last Position of Element in Sorted Array
"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]

        def findFirst():
            lo, hi = 0, len(nums)-1
            # key loop break when lo, hi adjecent
            while lo+1 < hi:
                md = lo + (hi-lo) // 2
                if nums[md] >= target:
                    hi = md
                else:
                    lo = md
            if nums[lo] == target: return lo
            if nums[hi] == target: return hi
            return -1

        def findLast():
            lo, hi = 0, len(nums)-1
            # key loop break when lo, hi adjecent
            while lo+1 < hi:
                md = lo + (hi-lo) // 2
                if nums[md] <= target:
                    lo = md
                else:
                    hi = md
            if nums[hi] == target: return hi
            if nums[lo] == target: return lo
            return -1
        first = findFirst()
        if first == -1: return [-1, -1]
        return [first, findLast()]
