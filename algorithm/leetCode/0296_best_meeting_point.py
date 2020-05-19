"""
296. Best Meeting Point
"""

from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = []
        cols = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        def sum_1D(r):
            r.sort()
            i, j = 0, len(r)-1
            ret = 0
            while i<j:
                ret += r[j]-r[i]
                i += 1
                j -= 1
            return ret

        return sum_1D(rows) + sum_1D(cols)

