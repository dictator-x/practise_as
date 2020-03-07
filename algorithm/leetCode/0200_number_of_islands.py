"""
200. Number of Islands
"""

from typing import List, Tuple

class Checker:
    def __init__(self, grid:List[List[str]]):
        self.t_bound, self.l_bound = 0, 0
        self.b_bound, self.r_bound = len(grid) - 1, len(grid[0]) - 1
        self.mask = [ [ False for _ in range(len(grid[0])) ] for _ in range(len(grid)) ]
        self.grid = grid


    def mark(self, point: Tuple[int, int]):
        x, y = point
        self.mask[x][y] = True

    def isMark(self, point: Tuple[int, int]) -> bool:
        x, y = point
        return self.mask[x][y]

    def canGo(self, src: Tuple[int, int], direction: Tuple[int, int]) -> bool:
        s_x, s_y = src
        d_x, d_y = direction
        x, y = s_x + d_x, s_y + d_y
        if x < self.t_bound or y < self.l_bound:
            return False
        if x > self.b_bound or y > self.r_bound:
            return False
        if self.grid[x][y] == "0":
            return False
        if self.isMark((x, y)):
            return False
        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        checker = Checker(grid)
        top = (-1, 0)
        left = (0, -1)
        bottom = (1, 0)
        right = (0, 1)
        ret = 0

        def go(src, step):
            s_x, s_y = src
            d_x, d_y = step
            return (s_x + d_x, s_y + d_y)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not checker.isMark((i, j)) and grid[i][j] != "0":
                    queue = []
                    queue.append((i, j))
                    checker.mark((i, j))
                    while len(queue) > 0:
                        point = queue.pop(0)
                        print(point)
                        if checker.canGo(point, top):
                            checker.mark(go(point,top))
                            queue.append(go(point, top))
                        if checker.canGo(point, bottom):
                            checker.mark(go(point, bottom))
                            queue.append(go(point, bottom))
                        if checker.canGo(point, left):
                            checker.mark(go(point, left))
                            queue.append(go(point, left))
                        if checker.canGo(point, right):
                            checker.mark(go(point,right))
                            queue.append(go(point, right))
                    ret += 1

        return ret
