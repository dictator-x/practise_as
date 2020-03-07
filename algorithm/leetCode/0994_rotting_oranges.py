"""
994. Rotting Oranges
"""

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = []
        ret = 0
        fresh = 0

        b_bound = len(grid)
        r_bound = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append(((i, j), 0))

        while len(queue) > 0:
            point, elapse = queue.pop(0)
            if elapse > ret:
                ret = elapse

            x, y = point

            if x - 1 >= 0 and grid[x-1][y] == 1:
                grid[x-1][y] == 2
                queue.append(((x-1, y), elapse + 1))
                fresh -= 1
            if x + 1 < b_bound and grid[x+1][y] == 1:
                grid[x+1][y] == 2
                queue.append(((x+1, y), elapse + 1))
                fresh -= 1
            if y - 1 > 0 and grid[x][y-1] == 1:
                grid[x][y-1] == 2
                queue.append(((x, y - 1), elapse + 1))
                fresh -= 1
            if y + 1 < r_bound and grid[x][y+1] == 1:
                grid[x][y+1] == 2
                queue.append(((x, y+1), elapse + 1))
                fresh -= 1


        return ret if fresh == 0 else -1
