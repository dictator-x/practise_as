"""
543. Diameter of Binary Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ret = 1
        def search(root):
            if not root: return 0
            nonlocal ret
            left = search(root.left)
            right = search(root.right)
            ret = max(ret, left+right+1)
            return 1 + max(left, right)
        search(root)
        return ret - 1
