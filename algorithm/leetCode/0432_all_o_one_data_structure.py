"""
432. All O`one Data Structure
"""
class Node:

    def __init__(self, value):
        self.pre = None
        self.post = None
        self.value = value
        self.keys = set([])

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # key -> node
        self.keys = {}
        self.head = None
        self.tail = None


    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.keys:
            if self.head == None:
                newNode = Node(1)
                self.head = self.tail = newNode
                newNode.keys.add(key)
                self.keys[key] = newNode
            elif self.head.value != 1:
                newNode = Node(1)
                self.head.pre = newNode
                newNode.post = self.head
                self.head = newNode
                newNode.keys.add(key)
                self.keys[key] = newNode
            else:
                self.head.keys.add(key)
                self.keys[key] = self.head
        else:
            curNode = self.keys[key]
            curNode.keys.discard(key)
            if curNode.post == None:
                newNode = Node(curNode.value + 1)
                newNode.pre = curNode
                curNode.post = newNode
                self.tail = newNode
                newNode.keys.add(key)
                self.keys[key] = newNode
            elif curNode.post.value != curNode.value + 1:
                print("key:" + key)
                newNode = Node(curNode.value + 1)
                newNode.pre = curNode
                newNode.post = curNode.post
                curNode.post.pre = newNode
                curNode.post = newNode
                newNode.keys.add(key)
                self.keys[key] = newNode
            else:
                curNode.post.keys.add(key)
                self.keys[key] = curNode.post

            # remove node if current node keys is empty
            if len(curNode.keys) == 0:
                if curNode == self.head:
                    curNode.post.pre = None
                    self.head = curNode.post
                else:
                    curNode.pre.post = curNode.post
                    curNode.post.pre = curNode.pre
                curNode.pre = None
                curNode.post = None

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.keys:
            return

        curNode = self.keys[key]
        curNode.keys.discard(key)

        # value == 1
        if curNode.value == 1:
            del self.keys[key]
        #value != 1
        else:
            if curNode.pre == None:
                newNode = Node(curNode.value-1)
                self.head = newNode
                curNode.pre = newNode
                newNode.post = curNode
                newNode.keys.add(key)
                self.keys[key] = newNode
            elif curNode.pre.value != curNode.value-1:
                newNode = Node(curNode.value-1)
                curNode.pre.post = newNode
                newNode.pre = curNode.pre
                newNode.post = curNode
                curNode.pre = newNode
                newNode.keys.add(key)
                self.keys[key] = newNode
            else:
                curNode.pre.keys.add(key)
                self.keys[key] = curNode.pre

        # Remove current node if keys is empty.
        if len(curNode.keys) == 0:
            if curNode == self.head and curNode == self.tail:
                self.head = self.head = None
            elif curNode == self.head:
                curNode.post.pre = None
                self.head = curNode.post
            elif curNode == self.tail:
                curNode.pre.post = None
                self.tail = curNode.pre
            else:
                curNode.pre.post = curNode.post
                curNode.post.pre = curNode.pre
            curNode.pre = None
            curNode.post = None

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return next(enumerate(self.tail.keys))[1] if self.tail != None else ""


    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return next(enumerate(self.head.keys))[1] if self.head != None else ""
