"""
149. Max Points on a Line
"""

from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        def tangle(p1, p2):
            """
            p1 and p2 should be different point.
            """
            p1x, p1y = p1
            p2x, p2y = p2

            if p1x == p2x:
                return 'infi'
            elif p1y == p2y:
                return '0'
            else:
                tx = p1x - p2x
                ty = p1y - p2y
                ret = tx/ty

            return ret

        ret = 0
        n = len(points)
        for i in range(n):
            tan = {}
            cur = 1
            lmax = 0
            for j in range(i+1, n):
                if points[i] == points[j]:
                    cur += 1
                else:
                    print(points[i])
                    print(points[j])
                    t = tangle(points[i], points[j])

                    if t not in tan:
                        tan[t] = 1
                    else:
                        tan[t] += 1
                    print(t)
                    print(tan[t])
                    lmax = max(lmax, tan[t])
            ret = max(ret, cur + lmax)

        return ret
