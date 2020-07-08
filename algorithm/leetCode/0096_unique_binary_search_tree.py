"""
96. Unique Binary Search Trees
"""

# TODO: There is O(n) method by math.copysign
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[0] = 1

        for i in range(2, n+1):
            dp[i] = sum([dp[j-1]*dp[i-j] for j in range(1,i+1)])

        return dp[-1]
