"""
272. Closest Binary Search Tree Value II
"""

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        ret = []

        def inorder(root):
            if root == None:
                return

            inorder(root.left)
            if k == len(ret):
                if abs(root.val - target) < abs(ret[0] - target):
                    ret.pop(0)
                # We can return early since the rest of sub-tree do not hold.
                else: return

            ret.append(root.val)

            inorder(root.right)

        inorder(root)
        return ret
