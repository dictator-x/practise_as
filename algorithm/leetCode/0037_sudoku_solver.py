"""
37. Sudoku Solver
"""

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [ [0] * 10 for _ in range(9) ]
        cols = [ [0] * 10 for _ in range(9) ]
        boxs = [ [0] * 10 for _ in range(9) ]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    d = int(board[i][j])
                    b = (i // 3) * 3 + j // 3
                    rows[i][d] = 1
                    cols[j][d] = 1
                    boxs[b][d] = 1

        def fill(i,j):
            if j == 9:
                return True

            ni = (i+1) % 9
            nj = j+1 if (i+1) == 9 else j

            if board[i][j] != ".": return fill(ni, nj)

            for z in range(1, 10):
                b = (i // 3) * 3 + j // 3
                if rows[i][z] != 1 and cols[j][z] != 1 and boxs[b][z] != 1:
                    rows[i][z] = 1
                    cols[j][z] = 1
                    boxs[b][z] = 1
                    board[i][j] = str(z)
                    # Important
                    if fill(ni, nj): return True
                    rows[i][z] = 0
                    cols[j][z] = 0
                    boxs[b][z] = 0
                    board[i][j] = "."

            return False

        fill(0,0)
