# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findStartingPoint(self, head):
        if not head:
            return None

        slow = fast = head

        # Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None  # No cycle

        # Find starting point of loop
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow