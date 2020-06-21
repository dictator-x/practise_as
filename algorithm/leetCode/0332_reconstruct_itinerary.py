"""
332. Reconstruct Itinerary
"""

from typing import List
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        children = defaultdict(list)

        for t in tickets:
            heappush(children[t[0]], t[1])

        ret = []

        def dfs(start):
            while children[start]:
                dfs(heappop(children[start]))

            ret.append(start)

        dfs("JFK")
        return ret[::-1]
