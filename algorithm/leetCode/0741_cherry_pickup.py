"""
741. Cherry Pickup
"""

from typing import List
import sys

# Think regular top-bottom solutin first, then use cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        min_infinite = -sys.maxsize

        # hint: r1 + c1 == r2 + c2
        dp = [ [ [ min_infinite for _ in range(n) ] for _ in range(n) ] for _ in range(n) ]

        def doPickup(r1, c1, r2):
            c2 = r1 + c1 - r2
            # Exceed boundary
            if r1 < 0 or c1 < 0 or r2 < 0 or c2 < 0:
                return -1
            # If block
            if grid[r1][c1] < 0 or grid[r2][c2] < 0:
                return -1
            # Reach end, only path reach here will start to calculate
            if r1 == 0 and c1 == 0:
                return grid[0][0]

            # Use cache result to reduce total time
            if dp[r1][c1][r2] != min_infinite:
                return dp[r1][c1][r2]

            # Calculate previous path
            pre = max(max(doPickup(r1-1, c1, r2 - 1), doPickup(r1, c1-1, r2)), \
                        max(doPickup(r1-1, c1, r2), doPickup(r1, c1-1, r2-1)))
            # If pre < 0 means no path to current position from [n-1][n-1]
            if pre < 0:
                # Cache result
                dp[r1][c1][r2] = -1
                return -1

            cur = pre + grid[r1][c1]
            # Add if they are not in the same cell
            if r1 != r2:
                cur += grid[r2][c2]

            # Cache result
            dp[r1][c1][r2] = cur
            return cur

        return max(0, doPickup(n-1, n-1, n-1))

if __name__ == "__main__":
    solution = Solution()
    grid = [[0, 1, -1],[1, 0, -1],[1, 1,  1]]
    print(solution.cherryPickup(grid))


