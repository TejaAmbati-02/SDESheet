# Definition of singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val    
        self.next = next  

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val        
        node.next = node.next.next

head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

sol = Solution()
sol.deleteNode(head.next)
curr = head
while curr:
    print(curr.val, end=" ")
    curr = curr.next
