"""
199. Binary Tree Right Side View
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []

        ret = []
        queue = [root]

        while queue:
            ret.append(queue[0].val)
            for _ in range(len(queue)):
                c = queue.pop(0)
                if c.right: queue.append(c.right)
                if c.left: queue.append(c.left)

        return ret
