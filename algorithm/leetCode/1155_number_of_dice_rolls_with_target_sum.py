"""
1155. Number of Dice Rolls With Target Sum
"""
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d or target > d*f:
            return 0

        # row = number of dice; column = target
        dp = [ [ 0 for _ in range(min(d*f, target) + 1) ] for _ in range(d+1) ]

        # fill initial value

        for i in range(d+1):
            dp[i][i] = 1

        # Inorder to avoid initial check, fill row 1
        for i in range(2, min(f, target) + 1):
            dp[1][i] = 1

        for i in range(2, d+1):
            for j in range(i+1, min(i*f, target)+1):
                t = 0
                for z in range(1, min(f, j) + 1):
                    t += dp[i-1][j-z]
                dp[i][j] = t

        print(dp)
        return dp[d][target] % (10**9 + 7)

if __name__ == "__main__":
    solution = Solution()
    print(solution.numRollsToTarget(5, 3, 7))
