"""
1041. Robot Bounded In Circle
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        x, y = 0, 0

        for c in instructions:
            if c == "L":
                d = (d+3)%4
            elif c == "R":
                d = (d+1)%4
            else:
                x, y = x + direction[d][0], y + direction[d][1]

        return True if ( x == 0 and y == 0 ) else False

