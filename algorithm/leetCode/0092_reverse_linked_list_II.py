"""
92. Reverse Linked List II
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        head1 = ListNode(0, head)
        t1 = head1
        for i in range(m-1):
            t1 = t1.next

        start = t1.next
        pre = None
        cur = start
        for _ in range(m, n+1):
            tmp = cur.next

            cur.next = pre
            pre = cur
            cur = tmp

        t1.next = pre
        start.next = cur

        return head1.next
