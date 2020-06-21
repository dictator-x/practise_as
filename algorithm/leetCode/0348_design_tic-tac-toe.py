"""
348. Design Tic-Tac-Toe
"""

class TicTacToe:

    def __init__(self, n: int):
        self.grid = [ [0]*n for _ in range(n)]


    def move(self, row: int, col: int, player: int) -> int:
        N = len(self.grid)
        self.grid[row][col] = player
        for i in range(N):
            if self.grid[row][i] != player: break
            if (i == N-1): return player

        for i in range(N):
            if self.grid[i][col] != player: break
            if (i == N-1): return player

        if row == col:
            for i in range(N):
                if self.grid[i][i] != player: break
                if (i == N-1): return player

        # reverse
        if row + col == N-1:
            for i in range(N):
                if self.grid[N-1-i][i] != player: break
                if (i == N-1): return player
        return 0
