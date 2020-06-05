from ..linked_list import LinkedListNode


def reverse_linked_list(node):

    if node is not None:
        reverse_linked_list(node.next)
        print(node.data)


def reverse(head):
    stack = []
    cur = head

    new_node = SinglyLinkedList()

    while cur.next:
        stack.append(cur.data)
        cur = cur.next

    while len(stack) > 0:
        new_node.insert_node(stack.pop())

    return new_node
