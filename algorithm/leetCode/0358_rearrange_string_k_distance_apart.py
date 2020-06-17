"""
358. Rearrange String k Distance Apart
"""

from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0 or k > len(s): return s

        fre_map = defaultdict(lambda: 0)
        for c in s:
            fre_map[c] += 1

        heap = []
        for key, val in fre_map.items():
            heappush(heap, (-val, key))

        ret = ""
        while heap:
            print(heap)
            temp = []
            for i in range(k):
                item = heappop(heap)
                fre, char = abs(item[0]), item[1]
                ret += char
                temp.append([fre-1, char])
                if not heap:
                    if not i == k-1 and not len(ret) == len(s):
                        return ""
                    else:
                        break

            for t in temp:
                if t[0] > 0:
                    heappush(heap,(-t[0], t[1]))

        return ret

