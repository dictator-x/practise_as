"""
99. Recover Binary Search Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        first = None
        second = None
        preNode = None
        while root != None:
            if root.left == None:
                if preNode and preNode.val > root.val:
                    first = root
                    if second is None:
                        second = preNode
                preNode = root
                root = root.right
            else:
                inorder_pre = root.left
                while inorder_pre.right != root and inorder_pre.right != None:
                    inorder_pre = inorder_pre.right

                if inorder_pre.right == None:
                    inorder_pre.right = root
                    root = root.left
                else:
                    inorder_pre.right = None
                    if preNode and preNode.val > root.val:
                        first = root
                        if second is None:
                            second = preNode
                    preNode = root
                    root = root.right
        first.val, second.val = second.val, first.val

