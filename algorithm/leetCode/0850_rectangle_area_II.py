"""
850. Rectangle Area II
"""

from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # All available x.
        x_points = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]] + [0]))

        x_i = {v: i for i, v in enumerate(x_points)}
        count = [0] * len(x_i)

        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, x1, x2, 1))
            events.append((y2, x1, x2, -1))
        events.sort()

        cur_y = 0
        cur_x_acc = 0
        area = 0

        # Calculate level by level in y.
        for y, x1, x2, sig in events:
            area += (y - cur_y) * cur_x_acc
            # Key step: remember events list is sort by y
            cur_y = y

            # Set avaliable x.
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sig

            # Calculate new x.
            cur_x_acc = sum(x2 - x1 if sig else 0 for x1, x2, sig in zip(x_points, x_points[1:], count))

        return area % (10**9 + 7)


