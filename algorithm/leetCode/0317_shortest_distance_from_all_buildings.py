"""
317. Shortest Distance from All Buildings
"""
from typing import List
import sys

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        dist = [ [0] * c for _ in range(r) ]
        nums = [ [0] * c for _ in range(r) ]
        totalBuidlings = 0

        def dfs(i, j):
            queue = [(i,j)]
            visited = [ [False] * c for _ in range(r) ]
            visited[i][j] = True
            # use to count distance from (i,j)
            distance = 0

            while len(queue) != 0:
                distance += 1

                for l in range(len(queue)):
                    cur_r, cur_c = queue.pop(0)
                    for d in direction:
                        new_r = cur_r + d[0]
                        new_c = cur_c + d[1]

                        if not isValid(new_r, new_c, visited): continue

                        queue.append((new_r, new_c))
                        dist[new_r][new_c] += distance
                        nums[new_r][new_c] += 1
                        visited[new_r][new_c] = True

        def isValid(i, j, visited):
            if i < 0 or j < 0: return False
            if i >= r or j >= c: return False
            if grid[i][j] != 0: return False
            if visited[i][j]: return False
            return True

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    totalBuidlings += 1
                    dfs(i, j)

        ret = sys.maxsize
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0 and nums[i][j] == totalBuidlings:
                    ret = min(ret, dist[i][j])

        return -1 if ret == sys.maxsize else ret
