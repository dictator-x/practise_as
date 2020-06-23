"""
289. Game of Life
"""

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                lives = 0

                for di in range(max(0,i-1), min(i+2, len(board))):
                    for dj in range(max(0,j-1), min(j+2, len(board[i]))):
                        lives += board[di][dj] & 1

                if lives == 3 or (lives - board[i][j]) == 3:
                    board[i][j] |= 2

        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = board[i][j] >> 1
