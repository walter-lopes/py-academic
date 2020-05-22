import unittest, os, sys
sys.path.append(os.path.abspath('exercises'))
from doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def test_insert_first(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_first(7)
        doubly_linked_list.insert_first(5)
        doubly_linked_list.insert_first(3)
        self.assertEqual(doubly_linked_list.head.data, 3)
        self.assertEqual(doubly_linked_list.tail.previous.data, 5)

    def test_remove_last(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_first(7)
        doubly_linked_list.insert_first(5)
        doubly_linked_list.insert_first(3)
        doubly_linked_list.remove_last()
        self.assertEqual(doubly_linked_list.head.data, 3)
        self.assertEqual(doubly_linked_list.tail.data, 5)
        self.assertEqual(doubly_linked_list.tail.previous.data, 3)
