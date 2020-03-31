"""
84. Largest Rectangle in Histogram
"""

from typing import List

# Hint: stack index.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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

        return ret

if __name__ == "__main__":
    solution = Solution()
    print(solution.largestRectangleArea([2,1,2]))
