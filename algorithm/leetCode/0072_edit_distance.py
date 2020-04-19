"""
72. Edit Distance
"""

import sys
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        r, c = len(word1), len(word2)
        max_int = sys.maxsize
        # we need to consider empty string case
        dp = [ [ max_int for _ in range(c+1) ] for _ in range(r+1) ]

        # "" -> "" has zero step
        dp[0][0] = 0

        # add only
        for i in range(1, c+1):
            dp[0][i] = i

        # remove only
        for i in range(1, r+1):
            dp[i][0] = i

        for i in range(1, r+1):
            for j in range(1, c+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] =  1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))

        return dp[r][c]
