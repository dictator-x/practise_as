"""
124. Binary Tree Maximum Path Sum
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        import sys
        if root == None:
            return 0

        ret = -sys.maxsize - 1
        def doFind(root):
            nonlocal ret
            if root == None:
                return 0

            l = max(0, doFind(root.left))
            r = max(0, doFind(root.right))
            cur = l + r + root.val
            ret = max(ret, cur)
            return max(l, r) + root.val

        doFind(root)
        return ret

