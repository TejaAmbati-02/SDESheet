# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, random=None):
#         self.val = val
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # original -> copy mapping
        mp = {}

        curr = head
        while curr:
            mp[curr] = ListNode(curr.val)
            curr = curr.next

        curr = head
        while curr:
            mp[curr].next = mp.get(curr.next)
            mp[curr].random = mp.get(curr.random)
            curr = curr.next

        return mp[head]