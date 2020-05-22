import unittest, os, sys
sys.path.append(os.path.abspath('.'))
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_insert_first(self):
        linked_list = LinkedList()
        linked_list.insert_first(2)
        linked_list.insert_first(1)
        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.tail.data, 2)

    def test_insert_first_tail(self):
        linked_list = LinkedList()
        linked_list.insert_first(2)
        self.assertEqual(linked_list.head.data, 2)
        self.assertEqual(linked_list.tail.data, 2)

    def test_insert_last(self):
        linked_list = LinkedList()
        linked_list.insert_first(2)
        linked_list.insert_last(3)
        linked_list.insert_last(4)
        self.assertEqual(linked_list.head.data, 2)
        self.assertEqual(linked_list.tail.data, 4)

    def test_remove_first(self):
        linked_list = LinkedList()
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.remove_first()
        self.assertEqual(linked_list.head.data, 2)
        self.assertEqual(linked_list.tail.data, 2)

    def test_remove_first_empty_list(self):
        linked_list = LinkedList()
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.remove_first()
        linked_list.remove_first()
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_remove_last(self):
        linked_list = LinkedList()
        linked_list.insert_first(2)
        linked_list.insert_first(5)
        linked_list.insert_first(3)
        linked_list.remove_last()
        self.assertEqual(linked_list.head.data, 3)
        self.assertEqual(linked_list.tail.data, 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)

