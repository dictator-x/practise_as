"""
1293. Shortest Path in a Grid with Obstacles Elimination
"""
from typing import List
import sys

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ret = 0
        directions = [(0, 1), (0,-1), (1, 0), (-1, 0)]
        obs = [ [sys.maxsize] * n for _ in range(m) ]

        queue = [(0, 0, 0)]

        while queue:
            queue_size = len(queue)
            print("------")
            print(queue)
            for _ in range(queue_size):
                cur_i, cur_j, ob = queue.pop(0)

                # Reach grid[-1][-1] return shortest path
                if cur_i == m - 1 and cur_j == n - 1:
                    return ret
                for direction in directions:
                    next_i, next_j = cur_i + direction[0], cur_j + direction[1]
                    if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n:
                        continue
                    next_ob = ob + grid[next_i][next_j]
                    # Key: This line of code also prevent infinite loop.
                    # next_ob > obs[next_i][next_j] will produce infinite
                    # loop.
                    if next_ob > k or nnext_ob >= obs[next_i][next_jext_ob >= obs[next_i][next_j]:
                        continue
                    obs[next_i][next_j] = next_ob
                    queue.append((next_i, next_j, next_ob))
            ret += 1
        # Can not find path
        return -1
