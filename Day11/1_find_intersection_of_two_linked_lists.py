class Node:
    def __init__(self, val):
        self.num = val
        self.next = None

def insertNode(head, val):
    newNode = Node(val)
    if not head:
        head = newNode
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newNode
    return head

def intersectionPresent(head1, head2):
    d1, d2 = head1, head2
    while d1 != d2:
        d1 = head2 if d1 is None else d1.next
        d2 = head1 if d2 is None else d2.next

    return d1  # If they meet, return the intersection node, otherwise None

def printList(head):
    while head and head.next:
        print(f"{head.num}->", end="")
        head = head.next
    if head:
        print(head.num, end="")
    print()

head = Node(1)
insertNode(head, 3)
insertNode(head, 1)
insertNode(head, 2)
insertNode(head, 4)
head1 = head
head = head.next.next.next  # Intersection point
headSec = Node(3)
head2 = headSec
headSec.next = head  # Creating intersection

print("List1: ", end="")
printList(head1)
print("List2: ", end="")
printList(head2)

answerNode = intersectionPresent(head1, head2)
if answerNode is None:
    print("No intersection")
else:
    print(f"The intersection point is {answerNode.num}")
