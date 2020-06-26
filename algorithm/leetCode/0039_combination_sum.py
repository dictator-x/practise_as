"""
39. Combination Sum
"""

from typing import List
from functools import lru_cache

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ret = []

        # @lru_cache(maxsize=None)
        def search(candidates, pre, target):
            if target == 0:
                ret.append(pre[:])

            for idx, c in enumerate(candidates):
                if target - c >= 0:
                    pre.append(c)
                    temp = candidates[:idx]
                    search(candidates[idx:], pre, target - c)
                    pre.pop()

        search(candidates, [], target)
        return ret
