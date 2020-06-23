"""
79. Word Search
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        n = len(board)
        m = len(board[0])

        def doSearch(i,j, idx, seen):
            if idx == len(word)-1 and board[i][j] == word[idx]: return True
            if board[i][j] != word[idx]: return False

            for d in directions:
                di, dj = i + d[0], j+d[1]
                if di < 0 or di >= n or dj < 0 or dj >= m: continue
                if (di, dj) in seen: continue

                seen.add((di, dj))
                if doSearch(di, dj, idx+1, seen): return True
                seen.remove((di, dj))

        for i in range(len(board)):
            for j in range(len(board[i])):
                if doSearch(i, j, 0, set([(i,j)])):
                    print(i,j)
                    return True

        return False
