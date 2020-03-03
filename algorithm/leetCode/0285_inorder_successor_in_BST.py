"""
285. Inorder Successor in BST
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        ret = None

        while root != None:
            if root.val <= p.val:
                root = root.right
            else:
                ret = root
                root = root.left

        return ret
