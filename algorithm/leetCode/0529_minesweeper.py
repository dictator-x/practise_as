"""
529. Minesweeper
"""

from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1,0), (-1, 0), (0, 1), (0,-1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
        directs = [(1,0), (-1, 0), (0, 1), (0,-1)]

        def check(board, x, y):
            ret = 0
            for i, j in directions:
                nx, ny = x+i, y+j
                if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]):
                    continue
                if board[nx][ny] == "M":
                    ret += 1
            return ret

        x, y = click[0], click[1]
        if board[x][y] == "M":
            board[x][y] = "X"
            return board

        if board[x][y] == "E":
            seen = set((x, y))
            queue = [(x, y)]

            while queue:
                cx, cy = queue.pop()
                nei = check(board, cx, cy)
                if nei != 0:
                    board[cx][cy] = str(nei)
                else:
                    board[cx][cy] = "B"
                    for i, j in directions:
                        nx, ny = cx+i, cy+j
                        if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]):
                            continue
                        if board[nx][ny] != "E" or (nx, ny) in seen:
                            continue
                        queue.append((nx, ny))
                        seen.add((nx, ny))
            return board

        return board
