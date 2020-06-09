"""
920. Number of Music Playlists
"""

class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        # dp[i][j]: using j songs create playlists whose length is equal to i.
        # ****: i is position of songs.
        # ****: answer is total number of possible
        # j: [1, N+1], i: [1, L+1]

        mod = 10**9 + 7
        dp = [ [0]*(N+1) for _ in range(L+1) ]

        # Initial
        dp[0][0] = 1

        # total i positions
        # 0 for all dp[i][j] where j > i
        for i in range(1, L+1):
            for j in range(1, N+1):
                dp[i][j] = dp[i-1][j-1]*(N-j+1) + dp[i-1][j]*max(0, j-K)

        return dp[L][N] % mod
