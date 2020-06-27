"""
143. Reorder List
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # Find middle.
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow

        # Reverse second part.
        pre = None
        cur = middle
        while cur:
            tmp = cur.next

            cur.next = pre
            pre = cur
            cur = tmp

        # Merge two list.
        l1, l2 = head, pre
        while l2 and l2.next:
            l1.next, l1 = l2, l1.next
            l2.next, l2 = l1, l2.next
