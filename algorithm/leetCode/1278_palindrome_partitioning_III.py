"""
1278. Palindrome Partitioning III
"""
import sys

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        cost = [ [0] * n for _ in range(n) ]

        # key: under stand this.
        # for l in range(2, n+1):
        #     for i in range(0, n):
        #         for j in range(i+1, n):
        #             cost[i][j] = cost[i+1][j-1] + (1 if s[i] != s[j] else 0)

        for l in range(2, n+1):
            for i in range(0, n-l+1):
                j = i + l - 1
                cost[i][j] = cost[i+1][j-1] + (1 if s[i] != s[j] else 0)

        dp = [ [200//2] * (n) for _ in range(k+1) ]

        for i in range(n):
            dp[1][i] = cost[0][i]

        for i in range(2, k+1):
            for j in range(0, n):
                for m in range(0, j):
                    dp[i][j] = min(dp[i][j], dp[i-1][m] + cost[m+1][j])
        return dp[k][n-1]

if __name__ == "__main__":
    solution = Solution()
    s = "aabbc"
    k = 2

    solution.palindromePartition(s,k)
