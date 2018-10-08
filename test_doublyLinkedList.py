from unittest import TestCase
from DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(TestCase):
    def test_len_empty(self):
        list = DoublyLinkedList()
        self.assertEqual(list.len(), 0)