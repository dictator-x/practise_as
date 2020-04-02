"""
221. Maximal Square
"""

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        dp = [ [ 0 for _ in range(len(matrix[0]) + 1) ] for _ in range(len(matrix) + 1) ]

        max_side = 0
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side

if __name__ == "__main__":
    grid = [["1", ""], ["1", "1"]]
    solution = Solution()
    print(solution.maximalSquare(grid))
