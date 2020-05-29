"""
489. Robot Room Cleaner
"""
class Solution:
    def cleanRoom(self, robot):
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        def helper(x, y, d):
            robot.clean()
            visited.add((x, y))

            for k in range(4):
                cur = ( k + d ) % 4
                # newX and newY should be base on current direction.
                newX = x + direction[cur][0]
                newY = y + direction[cur][1]

                if ((newX, newY) not in visited) and robot.move():
                    helper(newX, newY, cur)
                    # Return back
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    # reset direction
                    robot.turnRight()
                    robot.turnRight()

                # Change to next direction
                robot.turnRight()

        helper(0,0,0)
