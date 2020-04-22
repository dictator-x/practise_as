"""
403. Frog Jump
"""
from typing import List

# Idea: iterator all stones in sequece. create flags to the next store it can
# jumps.
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return False

        dp = {}
        # Initial set for each stone.
        for s in stones:
            dp[s] = set([])

        # Initial the very firt jump
        dp[0].add(0)

        for i in range(len(stones)):
            for last_step in dp[stones[i]]:
                for next_step in range(last_step-1, last_step+2):
                    # can not go negative
                    # flags next reachable stone
                    if next_step > 0 and (next_step + stones[i]) in dp:
                        dp.get(next_step + stones[i]).add(next_step)

        return True if len(dp[stones[-1]]) > 0 else False
