"""
85. Maximal Rectangle
"""

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Reuse code on leetcode84
        def largestRectangleArea(heights: List[int]) -> int:
            if not heights:
                return 0

            # Make code easier
            heights.append(0)
            # For smallest rectangle
            stack = [-1]
            ret = 0

            for i in range(len(heights)):
                while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                    top = stack.pop()
                    ret = max(ret, (i - stack[-1] - 1)*heights[top])
                stack.append(i)

            heights.pop()
            return ret

        if not matrix:
            return 0

        ret = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # This is the key for this code to word
                # You have to reset to 0 if the cell is 0
                # only accumulate sequence of "1" in a column
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0
            ret = max(ret, largestRectangleArea(dp))

        return ret

if __name__ == "__main__":
    grid = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    grid = [["0","1"],["1","0"]]
    solution = Solution()
    print(solution.maximalRectangle(grid))
