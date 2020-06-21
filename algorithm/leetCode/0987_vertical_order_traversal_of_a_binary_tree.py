"""
987. Vertical Order Traversal of a Binary Tree
"""

from typing import List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        def dfs(root, idx, idy, mem):
            if root.left: dfs(root.left, idx-1, idy+1, mem)
            mem[idx].append((idy, root.val))
            if root.right: dfs(root.right, idx+1, idy+1, mem)

        mem = defaultdict(list)
        dfs(root, 0, 0, mem)

        ret = []
        for key in sorted(mem.keys()):
            ret.append([ val[1] for val in sorted(mem[key])])

        return ret

