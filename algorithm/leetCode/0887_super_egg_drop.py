"""
887. Super Egg Drop
"""
# This solution do not accept by leetCdoe
import sys
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        dp = [ [ sys.maxsize for _ in range(N+1) ] for _ in range(K+1) ]

        # egg = 1, flood = infite
        for i in range(0, N+1):
            dp[1][i] = i
            dp[0][i] = 0

        # floadd = 1, egg = infite
        for i in range(0, K+1):
            dp[i][0] = 0

        for i in range(2, K+1):
            for j in range(1, N+1):
                l, h, m = 1, j, 0
                while l <= h:
                    m = l + (h-l)//2
                    b = dp[i-1][m-1]
                    nb = dp[i][j-m]
                    if b > nb:
                        h = m-1
                    else:
                        l = m+1
                    dp[i][j] = min(dp[i][j], max(b, nb) + 1)
                # for k in range(1, j+1):
                #     # two cases: egg break and not break
                #     dp[i][j] = min(dp[i][j], max(dp[i-1][k-1], dp[i][j-k]) + 1)

        return dp[K][N]

if __name__ == "__main__":
    solution = Solution()
    print(solution.superEggDrop(100, 10000))
