"""
727. Minimum Window Subsequence
"""

import sys

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        n_S = len(S)
        n_T = len(T)
        max_int = sys.maxsize // 2

        S = "#" + S
        T = "#" + T

        dp = [ [0] * (n_S+1) for _ in range(n_T+1) ]

        for i in range(1, n_T+1):
            dp[i][0] = max_int

        # We only looking for min number
        # so keeping + 1 will help us filter out who is minimal
        # dp[i][j] means min substring contain T[:i]
        for i in range(1, n_T+1):
            for j in range(1, n_S+1):
                if S[j] == T[i]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1] + 1

        # Iterate last row to find minimal dp[i][j]
        ret = max_int
        index = -1
        for i in range(1, n_S + 1):
            if dp[n_T][i] < ret:
                index = i
                ret = dp[n_T][i]

        return S[index-ret+1:index+1]



if __name__ == "__main__":
    S = "abcdebdde"
    T = "bde"
    solution = Solution()
    print(solution.minWindow(S, T))
