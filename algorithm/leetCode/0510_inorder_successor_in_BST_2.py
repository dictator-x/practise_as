"""
510. Inorder Successor in BST II
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def inorderSuccessor(self, node: Node) -> Node:
        ret = None

        if node.right != None:
            ret = node.right
            while ret.left != None:
                ret = ret.left
            return ret

        if node.parent != None:
            parent = node.parent
            while parent != None and parent.left != node:
                node = node.parent
                parent = node.parent
            if parent == None:
                return None
            else:
                return parent
        return None

