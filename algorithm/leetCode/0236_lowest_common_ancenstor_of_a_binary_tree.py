"""
236. Lowest Common Ancestor of a Binary Tree
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root):
            if not root or root.val == p.val or root.val == q.val:
                return root

            left = search(root.left)
            right = search(root.right)

            if not left: return right
            if not right: return left

            return root

        return search(root)
