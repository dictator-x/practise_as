"""
1197. Minimum Knight Moves
"""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]
        seen = set()
        ret = 0
        queue = [(0, 0)]

        while queue:
            ret += 1
            for _ in range(len(queue)):
                idx, idy = queue.pop(0)
                if (idx, idy) == (x, y): return ret-1
                for d in directions:
                    if (idx+d[0], idy+d[1]) in seen:
                        continue
                    seen.add((idx+d[0], idy+d[1]))
                    queue.append((idx+d[0], idy+d[1]))

        return ret


