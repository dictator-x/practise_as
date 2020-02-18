#2. Add Two Numbers

from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def traversaPrint(self):
        print(self.val)
        while self.next != None:
            self.next.traversaPrint()

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head1 = l1
        head2 = l2
        carryover = 0
        result = None
        current = None

        while head1 != None and head2 != None:
            i = head1.val + head2.val + carryover
            digit = i % 10
            carryover = i // 10

            if result == None:
                current = ListNode(digit)
                result = current
            else:
                current.next = ListNode(digit)
                current = current.next

            head1 = head1.next
            head2 = head2.next

        while head1 != None:
            i = head1.val + carryover
            digit = i % 10
            carryover = i // 10

            if result == None:
                current = ListNode(digit)
                result = current
            else:
                current.next = ListNode(digit)
                current = current.next
            head1 = head1.next

        while head2 != None:
            i = head2.val + carryover
            digit = i % 10
            carryover = i // 10

            if result == None:
                current = ListNode(digit)
                result = current
            else:
                current.next = ListNode(digit)
                current = current.next
            head2 = head2.next

        if carryover != 0:
            current.next = ListNode(carryover)

        return result



if __name__ == "__main__":
    solution = Solution()

