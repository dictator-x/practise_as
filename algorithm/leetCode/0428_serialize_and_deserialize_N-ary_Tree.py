"""
428. Serialize and Deserialize N-ary Tree
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        ret = []
        def doSerialize(root):
            if root == None:
                ret.append("None")
                return
            ret.append(str(root.val))
            ret.append(str(len(root.children) if root.children else 0))

            for i in range(len(root.children)):
                doSerialize(root.children[i])

        doSerialize(root)
        print(",".join(ret))
        return ",".join(ret)


    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        token = [ int(t) if t != "None" else None for t in data.split(",") ]
        print(token)

        def doDeserialize(token):
            if token[0] == None:
                token.pop(0)
                return None
            value = token.pop(0)
            child_len = token.pop(0)
            node = Node(value, [None]*child_len)

            for i in range(child_len):
                node.children[i] = doDeserialize(token)

            return node
        return doDeserialize(token)

