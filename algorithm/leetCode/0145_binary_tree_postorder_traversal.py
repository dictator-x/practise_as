"""
145. Binary Tree Postorder Traversal
"""

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []

        stack = [root]
        ret = []

        while stack:
            cur_node = stack.pop()
            ret.append(cur_node.val)
            if cur_node.left: stack.append(cur_node.left)
            if cur_node.right: stack.append(cur_node.right)
        return ret[::-1]
