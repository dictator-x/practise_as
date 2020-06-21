"""
173. Binary Search Tree Iterator
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        temp = root
        while temp:
            self.stack.append(temp)
            temp = temp.left


    def next(self) -> int:
        """
        @return the next smallest number
        """
        top = self.stack.pop()
        temp = top.right;
        while temp:
            self.stack.append(temp)
            temp = temp.left

        return top.val



    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stack: return True
        else: return False

