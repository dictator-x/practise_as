"""
545. Boundary of Binary Tree
"""

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        ret = [root.val]

        self.leftBound(root.left, ret)
        self.visitLeaves(root.left, ret)
        self.visitLeaves(root.right, ret)
        self.rightBound(root.right, ret)

        return ret

    def leftBound(self, root: TreeNode, ret: List[int]):
        if root == None or ( root.left == None and root.right == None ):
            return
        ret.append(root.val)
        if root.left != None:
            self.leftBound(root.left, ret)
        elif root.right != None:
            self.leftBound(root.right, ret)

    def rightBound(self, root: TreeNode, ret: List[int]):
        if root == None or (root.left == None and root.right == None):
            return
        if root.right != None:
            self.rightBound(root.right, ret)
        elif root.left != None:
            self.rightBound(root.left, ret)
        ret.append(root.val)

    def visitLeaves(self, root: TreeNode, ret: List[int]):
        if root == None:
            return
        if root.left == None and root.right == None:
            ret.append(root.val)

        self.visitLeaves(root.left, ret)
        self.visitLeaves(root.right, ret)
