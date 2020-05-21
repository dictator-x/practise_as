"""
980. Unique Paths III
"""

from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        non_obstacle = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: start = (i, j)
                if grid[i][j] == 0: non_obstacle += 1

        def dfs(i, j, non_obstacle):
            if i < 0 or j < 0 or i >= n or j >= m: return 0
            if grid[i][j] == 2:
                if non_obstacle < 0: return 1
                else: return 0
            if grid[i][j] == -1: return 0
            ret = 0
            grid[i][j] = -1

            for direction in directions:
                ret += dfs(i+direction[0], j+direction[1], non_obstacle-1)
            grid[i][j] = 0

            return ret

        return dfs(start[0], start[1], non_obstacle)

