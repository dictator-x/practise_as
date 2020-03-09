"""
460. LFU Cache
"""
import collections

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.fre = 1
        self.pre = None
        self.post = None
        self.list = None

    def removeFromList(self):
        self.list.removeNode(self)

    def __str__(self):
        return self.key + ":" + self.value + ":" + self.fre + ";"

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return True if self.head == None else False

    def addFront(self, node):
        node.list = self
        if self.head == None:
            self.head = self.tail = node
        else:
            node.post = self.head
            self.head.pre = node
            self.head = node
        self.count += 1

    def removeNode(self, node):
        if self.count == 1:
            self.head = self.tail = None
        else:
            if node == self.head:
                node.post.pre = None
                self.head = node.post
            elif node == self.tail:
                node.pre.post = None
                self.tail = node.pre
            else:
                node.post.pre = node.pre
                node.pre.post = node.post
        node.pre = node.post = None
        node.list = None
        self.count -= 1

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.fre_map = collections.defaultdict(lambda: DoubleList(), {})
        self.node_map = {}
        self.last = None
        self.count = 0


    def get(self, key: int) -> int:
        if self.cap < 1:
            return -1
        if key not in self.node_map:
            return -1
        else:
            node = self.node_map[key]
            if node != self.last:
                node.removeFromList()
                node.fre += 1
                next_fre_list = self.fre_map[node.fre]
                next_fre_list.addFront(node)
            else:
                if node.list.count > 1:
                    cur_fre_list = node.list
                    node.removeFromList()
                    node.fre += 1
                    next_fre_list = self.fre_map[node.fre]
                    next_fre_list.addFront(node)
                    self.last = cur_fre_list.tail
                else:
                    node.removeFromList()
                    node.fre += 1
                    next_fre_list = self.fre_map[node.fre]
                    next_fre_list.addFront(node)
                    self.last = next_fre_list.tail
            return node.value

    def put(self, key: int, value: int) -> None:
        if self.cap < 1:
            return
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self.get(key)
        else:
            new_node = Node(key, value)
            if self.count >= self.cap:
                remove_node = self.last
                remove_node.removeFromList()
                fre_list = self.fre_map[new_node.fre]
                if fre_list.count == 0:
                    fre_list.addFront(new_node)
                    self.last = new_node
                else:
                    fre_list.addFront(new_node)
                    self.last = fre_list.tail
                del self.node_map[remove_node.key]

            else:
                fre_list = self.fre_map[new_node.fre]
                if fre_list.count == 0:
                    fre_list.addFront(new_node)
                    self.last = new_node
                else:
                    fre_list.addFront(new_node)
                    self.last = fre_list.tail

            self.node_map[new_node.key] = new_node
            self.count += 1


if __name__ == "__main__":
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    print(cache.get(3))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
    # cache = LFUCache(2)
    # cache.put(1, 1)
    # cache.put(2, 2)
    # print(cache.last.key)
    # cache.get(1)
    # print(cache.last.key)
