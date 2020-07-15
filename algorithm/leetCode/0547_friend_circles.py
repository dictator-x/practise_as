"""
547. Friend Circles
"""

from typing import List

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [False] * len(M)
        ret = 0

        for i in range(len(M)):
            if not visited[i]:
                visited[i] = True
                queue = [i]
                while queue:
                    cur = queue.pop(0)
                    for idx, val in enumerate(M[cur]):
                        if not visited[idx] and val:
                            visited[idx] = True
                            queue.append(idx)

                ret += 1
        return ret
