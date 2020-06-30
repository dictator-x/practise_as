"""
442. Find All Duplicates in an Array
"""

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # count value instead of index
        for val in nums:
            nums[abs(val)-1] *= -1

        ret = []
        for val in nums:
            if nums[abs(val)-1] > 0:
                ret.append(abs(val))
                nums[abs(val)-1] *= -1
        return ret
