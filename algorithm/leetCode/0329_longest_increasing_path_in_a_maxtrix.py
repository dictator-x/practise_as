"""
329. Longest Increasing Path in a Matrix
"""
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        ni, nj = len(matrix), len(matrix[0])
        dp = [ [ -1 ] * nj for _ in range(ni) ]
        ret = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(i, j):
            if dp[i][j] != -1: return dp[i][j]
            # protect reverse.
            dp[i][j] = 1

            for d in directions:
                di = i + d[0]
                dj = j + d[1]
                if di < 0 or di >= ni or dj < 0 or dj >= nj or matrix[di][dj] <= matrix[i][j]: continue
                dp[i][j] = max(dp[i][j], 1+dfs(di,dj))
            return dp[i][j]

        for i in range(ni):
            for j in range(nj):
                ret = max(ret, dfs(i,j))
        return ret
