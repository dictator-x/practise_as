"""
863. All Nodes Distance K in Binary Tree
"""

from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = defaultdict(set)
        queue = [root]

        while queue:
            cur = queue.pop(0)

            if cur.left:
                graph[cur.val].add(cur.left.val)
                graph[cur.left.val].add(cur.val)
                queue.append(cur.left)

            if cur.right:
                graph[cur.val].add(cur.right.val)
                graph[cur.right.val].add(cur.val)
                queue.append(cur.right)

        queue = [target.val]
        seen  = set([target.val])
        i = 0
        while queue and i < K:
            i += 1
            for _ in range(len(queue)):
                cur = queue.pop(0)
                for child in graph[cur]:
                    if child not in seen:
                        queue.append(child)
                        seen.add(child)

        return [ val for val in queue ]
