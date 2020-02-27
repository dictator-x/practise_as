"""
238. Product of Array Except Self
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        if n < 2:
            return nums

        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        ret = [0] * n
        for i in range(0, n):
            ret[i] = left[i] * right[i]

        return ret
