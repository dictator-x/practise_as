"""
1206. Design Skiplist
"""

from random import randint

class Node:
    def __init__(self, key, next=None, down=None):
        self.key = key
        self.next = next
        self.down = down

class Skiplist:

    def __init__(self):
        self.head = Node(-1)

    def search(self, target: int) -> bool:
        cur_node = self.head
        while cur_node:
            next_node = cur_node.next
            # Search in same level
            while next_node and target > next_node.key:
                next_node = next_node.next
                cur_node = cur_node.next

            if next_node and target == next_node.key: return True
            cur_node = cur_node.down

        return False


    def add(self, num: int) -> None:
        # use to record jump point.
        jumpNodes = []

        cur_node = self.head
        while cur_node:
            next_node = cur_node.next
            # Search in same level
            while next_node and num > next_node.key:
                next_node = next_node.next
                cur_node = cur_node.next

            jumpNodes.append(cur_node)
            # Jump to next level
            cur_node = cur_node.down

        down_node = None
        # Update levels.
        for i in range(len(jumpNodes)-1,-1,-1):
            # Add node into cur level.
            cur_node = jumpNodes[i]
            new_node = Node(num, cur_node.next, down_node)
            cur_node.next = new_node
            down_node = new_node

            # try promote
            promote = randint(0,1)
            if promote == 0: break
            if i == 0:
                # create a new level.
                new_node = Node(num, None, down_node)
                self.head = Node(-1, new_node, self.head)


    def erase(self, num: int) -> bool:
        flag = False
        cur_node = self.head
        while cur_node:
            next_node = cur_node.next
            while next_node and num > next_node.key:
                next_node = next_node.next
                cur_node = cur_node.next

            if next_node and num == next_node.key:
                cur_node.next = next_node.next
                flag = True

            cur_node = cur_node.down

        return flag
