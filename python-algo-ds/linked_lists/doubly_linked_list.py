class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, data_node):
        node = DoublyLinkedListNode(data_node)

        temp = self.head

        self.head = node

        self.head.next = temp

        if not self.tail:
            self.tail = self.head
        else:
            temp.previous = self.head

    def remove_last(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None

        self.tail.previous.next = None
        self.tail = self.tail.previous


class DoublyLinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

