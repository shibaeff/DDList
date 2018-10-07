from unittest import TestCase
from DoublyLinkedList import Item


class TestItem(TestCase):
    def test_creation(self):
        """
        Test creation of the item object
        :return:
        """
        prev = Item()
        next = Item()
        item = Item(next_item=next, prev_item=prev, element="Something")

    def test_element(self):
        # creating Item with init config

        self.fail()

    def test_next_item(self):
        self.fail()

    def test_prev_item(self):
        self.fail()
