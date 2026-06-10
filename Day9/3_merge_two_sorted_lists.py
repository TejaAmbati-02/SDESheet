class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

def sort_two_linked_lists(list1, list2):
    dummy_node = Node(-1)
    temp = dummy_node

    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next

    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2
    return dummy_node.next

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    list1 = Node(1)
    list1.next = Node(3)
    list1.next.next = Node(5)

    list2 = Node(2)
    list2.next = Node(4)
    list2.next.next = Node(6)

    print("First sorted linked list: ", end="")
    print_linked_list(list1)

    print("Second sorted linked list: ", end="")
    print_linked_list(list2)

    merged_list = sort_two_linked_lists(list1, list2)

    print("Merged sorted linked list: ", end="")
    print_linked_list(merged_list)