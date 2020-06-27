"""
767. Reorganize String
"""

from collections import defaultdict
from math import ceil
from heapq import heappop, heappush

class Solution:
    def reorganizeString(self, S: str) -> str:
        record = defaultdict(lambda: 0)
        max_char = 0
        for c in S:
            record[c] += 1
            max_char = max(max_char, record[c])
        if max_char > ceil(len(S)/2): return ""

        heap = []
        for key, val in record.items():
            heappush(heap, (-val, key))

        ret = [None]*len(S)
        #First fill oven, then odd
        t = 0
        while heap:
            count, char = heappop(heap)
            count = -count
            for _ in range(count):
                if t >= len(S): t = 1
                ret[t] = char
                t += 2
        return "".join(ret)
