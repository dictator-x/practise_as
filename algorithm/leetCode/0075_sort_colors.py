"""
75. Sort Colors
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        b, m, e = 0, 0, len(nums)-1

        while m <= e:
            if b < m and nums[m] == 0:
                nums[m], nums[b] = nums[b], nums[m]
                b += 1
            elif nums[m] == 2:
                nums[m], nums[e] = nums[e], nums[m]
                e -= 1
            else:
                m += 1
