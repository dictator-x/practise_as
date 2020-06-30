"""
445. Add Two Numbers II
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []

        temp = l1
        while temp:
            stack1.append(temp.val)
            temp = temp.next

        temp = l2
        while temp:
            stack2.append(temp.val)
            temp = temp.next

        carry = 0
        tail = None
        while stack1 and stack2:
            val = stack1.pop() + stack2.pop() + carry
            carry = 1 if val > 9 else 0
            digit = val % 10

            tail = ListNode(digit, tail)

        while stack1:
            val = stack1.pop() + carry
            carry = 1 if val > 9 else 0
            digit = val % 10

            tail = ListNode(digit, tail)

        while stack2:
            val = stack2.pop() + carry
            carry = 1 if val > 9 else 0
            digit = val % 10

            tail = ListNode(digit, tail)

        if carry > 0:
            tail = ListNode(carry, tail)

        return tail

