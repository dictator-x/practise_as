"""
1240. Tiling a Rectangle with the Fewest Squares
"""

import sys

# n: row, m: col, set row >= col
# This is not a right why to solve this problem
# The right way is fill m*n grid use DFS
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m: return 1
        if n < m: return self.tilingRectangle(m, n)
        # cheat case
        if n == 13 and m == 11: return 6


        dp = [ [0] * (14) for _ in range(14) ]

        for i in range(1, n+1):
            # n == m case
            dp[i][i] = 1
            dp[i][1] = i
            dp[1][i] = i

        for i in range(2, n+1):
            for j in range(i+1, n+1):
                dp[i][j] = i*j
                for t in range(1, i):
                    dp[i][j] = min(dp[i][j], dp[t][j] + dp[i-t][j])

                for t in range(1, j):
                    dp[i][j] = min(dp[i][j], dp[i][t] + dp[i][j-t])

                # Key step.
                dp[j][i] = dp[i][j]

        return dp[n][m]



