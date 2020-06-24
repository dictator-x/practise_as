"""
46. Permutations
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def search(remain, p):
            if not remain: ret.append(p[:])

            for i in range(len(remain)):
                choose = remain.pop(i)
                p.append(choose)
                search(remain, p)
                p.pop()
                remain.insert(i, choose)

        search(nums, [])
        return ret
