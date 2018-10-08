from unittest import TestCase
from DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(TestCase):
    def test_len_empty(self):
        list = DoublyLinkedList()
        self.assertEqual(list.len(), 0)

    def test_empty_first_last(self):
        list = DoublyLinkedList()
        from Exceptions.exceptions import EmptyListOperationError
        with self.assertRaises(EmptyListOperationError):
            print(list.first())
        with self.assertRaises(EmptyListOperationError):
            print(list.last())

    def test_push_1(self):
        list = DoublyLinkedList()
        for i in range(1000):
            list.push(i)
        self.assertEqual(1000, list.len())