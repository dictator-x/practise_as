"""
695. Max Area of Island
"""

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        direction = [(0,1), (0, -1), (1, 0), (-1, 0)]
        n = len(grid)
        m = len(grid[0])

        def search(point):
            if point in seen or grid[point[0]][point[1]] == 0: return 0

            ret = 0
            stack = [(point[0], point[1])]
            seen.add((point[0], point[1]))

            while stack:
                i, j = stack.pop()
                ret += 1
                for di, dj in direction:
                    ni = i + di
                    nj = j + dj
                    if ni < 0 or nj < 0 or ni >= n or nj >= m or grid[ni][nj] == 0 or (ni, nj) in seen:
                        continue
                    seen.add((ni, nj))
                    stack.append((ni, nj))
            return ret
        return max([ search((i,j)) for i in range(n) for j in range(m) ])
