"""
1229. Meeting Scheduler
"""

from typing import List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        join_set = []
        slots1.sort(key=lambda i: (i[0], i[1]))
        slots2.sort(key=lambda i: (i[0], i[1]))

        while slots1 and slots2:
            if slots1[0][1] < slots2[0][0]: slots1.pop(0)
            elif slots2[0][1] < slots1[0][0]: slots2.pop(0)
            else:
                l = max(slots1[0][0], slots2[0][0])
                r = min(slots1[0][1], slots2[0][1])
                join_set.append([l, r])
                if slots1[0][1] < slots2[0][1]: slots1.pop(0)
                else: slots2.pop(0)
        print(join_set)
        for l, r in join_set:
            if r - l >= duration: return [l, l+duration]

        return []


