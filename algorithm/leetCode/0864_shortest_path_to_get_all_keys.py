"""
864. Shortest Path to Get All Keys
"""

from typing import List
from copy import deepcopy

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        gg = []
        for s in grid:
            gg.append([])
            for c in s:
                gg[-1].append(c)
        grid = gg
        print(grid)
        m, n = len(grid), len(grid[0])
        ret = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        start = None
        keys = set()
        dp = [ [ [ False for _ in range(2 << 5) ] for _ in range(n) ]  for _ in range(m) ]

        def getOffset(char):
            return ord(char) - ord("a")

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@": start = (i, j)
                elif grid[i][j].islower(): keys.add(grid[i][j])

        queue = [(start[0], start[1], 0)]
        while queue:
            queue_size = len(queue)
            for _ in range(queue_size):
                # print(queue[0])
                cur_i, cur_j, cur_key = queue.pop(0)
                if bin(cur_key)[2:].count("1") == len(keys): return ret

                for direction in directions:
                    next_i, next_j = cur_i + direction[0], cur_j + direction[1]

                    if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n or grid[next_i][next_j] == "#":
                        continue

                    if grid[next_i][next_j].isupper() and (1 << getOffset(grid[next_i][next_j].lower())) & cur_key == 0:
                        continue

                    next_key = cur_key

                    if grid[next_i][next_j].islower():
                        next_key = cur_key | ( 1 << getOffset(grid[next_i][next_j]))

                    # TODO: wrong
                    if dp[next_i][next_j][next_key]:
                        continue

                    dp[next_i][next_j][next_key] = True
                    queue.append((next_i, next_j, next_key))

            ret += 1

        return -1
