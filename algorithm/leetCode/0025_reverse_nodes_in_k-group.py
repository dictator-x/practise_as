# 25. Reverse Nodes in k-Group

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None or k <= 1:
            return head

        temp_head = ListNode(0)
        temp_head.next = head
        head = temp_head
        group = head

        while True:
            start = group.next
            length = 0
            lookahead = group
            while lookahead.next and length < k:
                lookahead = lookahead.next
                length += 1

            if length < k or lookahead == None:
                break

            pre = start
            cur = start.next
            for i in range(0, k-1):
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp

            group.next = pre
            start.next = cur

            group = start


        return head.next



