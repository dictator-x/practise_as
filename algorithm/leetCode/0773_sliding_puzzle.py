"""
773. Sliding Puzzle
"""

from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        initial = ""
        end = "123450"
        zero = None

        for i in range(len(board)):
            for j in range(len(board[i])):
                initial += str(board[i][j])
                if board[i][j] == 0:
                    zero = (i, j)

        top, down = 0, 1
        left, right = 0, 2

        def index2position(index):
            return (index//3, inex%3)

        def position2index(position):
            return position[0]*3 + position[1]

        def move(cur, to):
            return ( cur[0] + to[0], cur[1] + to[1] )

        def stringMove(cur_string, fr, to):
            a = position2index(fr)
            b = position2index(to)
            strlst = list(cur_string)
            strlst[a], strlst[b] = strlst[b], strlst[a]
            return "".join(strlst)

        def outOfBound(position):
            x, y = position
            if x < 0 or x > 1:
                return True
            if y < 0 or y > 2:
                return True
            return False


        queue = [(initial, zero)]
        visited = set([])

        step = 0
        while len(queue) > 0:
            step += 1

            for i in range(len(queue)):
                puzzle, zero_position = queue.pop(0)
                if puzzle == end:
                    return step - 1

                zero_move_top = move(zero_position, (-1, 0))
                zero_move_down = move(zero_position, (1, 0))
                zero_move_left = move(zero_position, (0, -1))
                zero_move_right = move(zero_position, (0, 1))

                new_puzzle = ""
                if not outOfBound(zero_move_top):
                    new_puzzle = stringMove(puzzle, zero_position, zero_move_top)
                    if new_puzzle not in visited:
                        queue.append((new_puzzle, zero_move_top))
                        visited.add(new_puzzle)

                if not outOfBound(zero_move_down):
                    new_puzzle = stringMove(puzzle, zero_position, zero_move_down)
                    if new_puzzle not in visited:
                        queue.append((new_puzzle, zero_move_down))
                        visited.add(new_puzzle)

                if not outOfBound(zero_move_left):
                    new_puzzle = stringMove(puzzle, zero_position, zero_move_left)
                    if new_puzzle not in visited:
                        queue.append((new_puzzle, zero_move_left))
                        visited.add(new_puzzle)

                if not outOfBound(zero_move_right):
                    new_puzzle = stringMove(puzzle, zero_position, zero_move_right)
                    if new_puzzle not in visited:
                        queue.append((new_puzzle, zero_move_right))
                        visited.add(new_puzzle)
        return -1

if __name__ == "__main__":
    solution = Solution()
    # print(solution.slidingPuzzle([[1,2,3],[5,4,0]]))
    # print(solution.slidingPuzzle([[1,2,3],[4,0,5]])
    print(solution.slidingPuzzle([[4,1,2],[5,0,3]]))
