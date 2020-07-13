"""
148. Sort List
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        def middle(head):
            slow, fast = head, head
            while fast and fast.next and fast.next.next:
                print(fast.val)
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge(list1, list2):
            ret = ListNode()
            temp = ret
            while list1 and list2:
                if list1.val < list2.val:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    list2 = list2.next
                temp = temp.next

            temp.next = list1 or list2
            return ret.next

        middle_node = middle(head)
        right = middle_node.next
        #Important: break inner connection.
        middle_node.next = None
        return merge(self.sortList(head), self.sortList(right))
