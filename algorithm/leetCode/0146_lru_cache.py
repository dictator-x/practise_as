"""
146. LRU Cache
"""

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.pre = None
        self.post = None

class LRUCache:

    def __init__(self, capacity: int):
        self.count = 0
        self.capacity = capacity
        self.m = {}
        self.head = None
        self.tail = None


    def get(self, key: int) -> int:
        if key in self.m:
            n = self.m[key]
            if n.pre != None:
                n.pre.post = n.post
                if n.post == None:
                    self.tail = n.pre
                else:
                    n.post.pre = n.pre
                n.pre = None
                n.post = None
                n.post = self.head
                self.head.pre = n
                self.head = n
            return n.value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if self.capacity < 1:
            return
        if key in self.m:
            node = self.m[key]
            node.value = value
            self.get(key)
            return

        if self.count == self.capacity:
            if ( self.head == self.tail ):
                del self.m[self.head.key]
                node = Node(key, value)
                self.head = self.tail = node
                self.m[key] = node
                return
            # TODO: remove tail and add
            last = self.tail
            last.pre.post = None
            self.tail = last.pre
            last.pre = None
            last.post = None
            del self.m[last.key]

            node = Node(key, value)
            self.m[key] = node
            node.post = self.head
            self.head.pre = node
            self.head = node
        else:
            node = Node(key, value)
            self.m[key] = node
            if self.head == None:
                self.head = self.tail = node
            else:
                node.post = self.head
                self.head.pre = node
                self.head = node
            self.count += 1

    def print(self):
        tmp = self.head
        while tmp != None:
            print(tmp.value)
            tmp = tmp.post

    def printR(self):
        tmp = self.tail
        while tmp != None:
            print(tmp.value)
            tmp = tmp.pre

if __name__ == "__main__":
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    print (">>>")
    cache.print()
    print ("----")
    cache.printR()
    print ("***")

    print ( cache.get(1) )
    print (">>>")
    cache.print()
    print ("----")
    cache.printR()
    print ("***")
    cache.put(3, 3)
    print ( cache.get(2) )
    print (">>>")
    cache.print()
    print ("----")
    cache.printR()
    print ("***")
    cache.put(4, 4)
    print ( cache.get(1) )
    print ( cache.get(3) )
    print ( cache.get(4) )

