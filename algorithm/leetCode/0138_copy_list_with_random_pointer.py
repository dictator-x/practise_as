"""
138. Copy List with Random Pointer
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        visited = {}

        def copy(node):
            if node == None:
                return None
            elif node in visited:
                return visited[node]
            else:
                new_node = Node(node.val, None, None)
                visited[node] = new_node
                return new_node


        dummy = Node(-1, None, None)
        cur = dummy

        while head != None:
            cur.next = copy(head)
            cur.next.random = copy(head.random)
            head = head.next
            cur = cur.next

        return dummy.nextclass Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        visited = {}

        def copy(node):
            if node == None:
                return None
            elif node in visited:
                return visited[node]
            else:
                new_node = Node(node.val, None, None)
                visited[node] = new_node
                return new_node


        dummy = Node(-1, None, None)
        cur = dummy

        while head != None:
            cur.next = copy(head)
            cur.random = copy(head.random)
            head = head.next
            cur = cur.next

        return dummy.next
