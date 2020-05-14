"""
305. Number of Islands II
"""

from typing import List

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ret = []
        n_dis = [-1] * (m*n)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0

        def findRoot(idx):
            return n_dis[idx] if idx == n_dis[idx] else findRoot(n_dis[idx])

        for position in positions:
            cur_idx = position[0]*n + position[1]
            # Important
            if n_dis[cur_idx] != -1:
                ret.append(count)
                continue

            # assign default root to itself index
            count += 1
            n_dis[cur_idx] = cur_idx

            # find if it can be an island with neighbour cell
            for d in directions:
                i, j = position[0] + d[0], position[1] + d[1]
                next_idx = i*n + j
                if i < 0 or i >= m or j < 0 or j >= n or n_dis[next_idx] == -1:
                    continue
                cur_parent = findRoot(cur_idx)
                next_parent = findRoot(next_idx)
                print(cur_idx, next_idx)
                # key: n_dis[cur_parent] = next_parent will be wrong
                if cur_parent != next_parent:
                    n_dis[next_parent] = cur_parent
                    count -= 1


            ret.append(count)
        print(n_dis)

        return ret
