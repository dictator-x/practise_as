"""
31. Next Permutation
"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse(i,j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        N = len(nums)
        i = N-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            j = N-1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        reverse(i+1, N-1)
