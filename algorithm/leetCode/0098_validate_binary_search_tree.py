"""
98. Validate Binary Search Tree
"""
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):

        if not root: return True
        # carry left and right limit
        stack = [(root, -sys.maxsize, sys.maxsize)]

        while stack:
            cur, l_bound, r_bound = stack.pop()

            if not cur: continue

            if cur.val <= l_bound or cur.val >= r_bound:
                return False

            stack.append((cur.left, l_bound, cur.val))
            stack.append((cur.right, cur.val, r_bound))

        return True
