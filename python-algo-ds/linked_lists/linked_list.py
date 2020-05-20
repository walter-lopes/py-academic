class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, node_data):
        node = LinkedListNode(node_data)

        temp = self.head

        self.head = node
        self.head.next = temp

        if not self.tail:
            self.tail = self.head

    def insert_last(self, node_data):
        node = LinkedListNode(node_data)

        if not self.head:
            self.head = node

        else:
            self.tail.next = node

        self.tail = node

    def remove_first(self):
        if self.head:
            self.head = self.head.next

            if not self.head:
                self.tail = None

    def remove_last(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None

            else:
                curr = self.head
                while curr.next != self.tail:
                    curr = curr.next

                curr.next = None
                self.tail = curr


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None
