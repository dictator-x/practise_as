"""
103. Binary Tree Zigzag Level Order Traversal
"""

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        queue = [root]
        ret = []
        while queue:
            ret.append([])
            for _ in range(len(queue)):
                cur = queue.pop(0)
                ret[-1].append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)

        for i in range(1, len(ret), 2):
            ret[i] = ret[i][::-1]
        return ret

