"""
78. Subsets
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]

        for n in nums:
            ret += [ i + [n] for i in ret ]
        return ret
