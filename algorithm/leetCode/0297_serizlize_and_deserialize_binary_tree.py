"""
297. Serialize and Deserialize Binary Tree
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        ret = []

        def doSerialize(root):
            if root == None:
                ret.append("None")
                return

            ret.append(str(root.val))
            doSerialize(root.left)
            doSerialize(root.right)

        doSerialize(root)
        return ",".join(ret)

    def deserialize(self, data):
        data = [ ( int(i) if i != "None" else None ) for i in data.split(",") ]
        def doDeserialize(data):
            val = data.pop(0)
            if val == None:
                return None
            else:
                node = TreeNode(val)
                node.left = doDeserialize(data)
                node.right = doDeserialize(data)
                return node

        return doDeserialize(data)
