# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Solution:
    def merge(self, a, b):
        dummy = ListNode(-1)
        curr = dummy

        while a and b:
            if a.val <= b.val:
                curr.child = a
                a = a.child
            else:
                curr.child = b
                b = b.child

            curr = curr.child
            curr.next = None

        if a:
            curr.child = a
        else:
            curr.child = b

        return dummy.child

    def flattenLinkedList(self, head):
        if not head or not head.next:
            return head

        # Flatten the remaining list
        head.next = self.flattenLinkedList(head.next)

        # Merge current list with flattened list
        head = self.merge(head, head.next)

        return head