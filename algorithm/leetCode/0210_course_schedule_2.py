"""
210. Course Schedule II
"""

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [ i for i in range(numCourses) ]

        graph = {}
        in_degree = {}
        ret = []

        for i in range(numCourses):
            graph[i] = set([])
            in_degree[i] = 0

        for i in range(len(prerequisites)):
            dependency = prerequisites[i]
            graph[dependency[1]].add(dependency[0])
            in_degree[dependency[0]] += 1

        queue = []
        for key in in_degree:
            if in_degree[key] == 0:
                queue.append(key)

        ret = []
        while len(queue) > 0:
            cur = queue.pop(0)
            ret.append(cur)

            for child in graph[cur]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        return ret if len(ret) == numCourses else []


if __name__ == "__main__":
    test_arg1 = 2
    test_arg2 = [[1,0]]
    test_arg1 = 2
    test_arg2 = [[1,0],[2,0],[3,1],[3,2]]
    test_arg1 = 3
    test_arg2 = [[1,0]]
    solution = Solution()
    print(solution.findOrder(test_arg1, test_arg2))
