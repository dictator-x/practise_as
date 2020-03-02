"""
314. Binary Tree Vertical Order Traversal
"""

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        hashMap = {}
        queue = []
        ret = []
        v_index = 0

        queue.append((root, v_index));

        while len(queue) > 0:
            root, v_index = queue.pop(0)

            if v_index not in hashMap:
                hashMap[v_index] = [root.val]
            else:
                hashMap[v_index].append(root.val)

            if root.left != None:
                queue.append((root.left, v_index - 1))
            if root.right != None:
                queue.append((root.right, v_index + 1))

        for key in sorted(hashMap.keys()):
            ret.append(hashMap[key])

        return ret

if __name__ == "__main__":
    solution = Solution()
    solution.verticalOrder(None)
