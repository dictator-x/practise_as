"""
234. Palindrome Linked List
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ret = []

        while head:
            ret.append(head.val)
            head = head.next

        return ret == ret[::-1]
