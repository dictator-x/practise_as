"""
55. Jump Game
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums) - 1

        max_seen = 0
        cur_seen = 0

        for idx, val in enumerate(nums):
            max_seen = max(idx+val, max_seen)
            if cur_seen == idx:
                cur_seen = max_seen
        return True if cur_seen >= N else False
