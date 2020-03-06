"""
23. Merge k Sorted Lists
"""

from typing import List
from heapq import heappush, heappop

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        priorityQueue = []
        head = cur = ListNode(0)

        for i, l in enumerate(lists):
            if l:
                heappush(priorityQueue, (l.val, i))

        while len(priorityQueue) > 0:
            val, i = heappop(priorityQueue)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[i] = lists[i].next
            if node:
                heappush(priorityQueue, (node.val, i))
        return head.next

class Solution2:
    def merge2ListNode(self, head1: ListNode, head2: ListNode) -> ListNode:
        result = cur = ListNode(0)

        while head1 and head2:
            if head1.val =< head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next

        if head1:
            cur.next = head1
        elif head2:
            cur.next = head2

        return result.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        amount = len(lists)
        interval = 1

        while interval < amount:
            for i in range(0, amount-interval, 2*interval):
                lists[i] = self.merge2ListNode(lists[i], lists[i+interval])
            interval = interval * 2

        if amount > 0:
            return lists[0]
        else:
            return None

if __name__ == "__main__":
    solution = Solution()
    # solution.mergeKList()
