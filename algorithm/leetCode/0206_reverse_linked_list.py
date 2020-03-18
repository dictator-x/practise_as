"""
206. Reverse Linked List
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head == None:
            return None

        cur = head
        next = head.next

        while next != None:
            tmp = next.next
            next.next = cur

            cur = next
            next = tmp

        head.next = None
        return cur
