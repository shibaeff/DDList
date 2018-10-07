from unittest import TestCase
from DoublyLinkedList import Item


class TestItem(TestCase):
    def test_creation(self):
        """
        Test creation of the item object
        :return:
        """
        from Exceptions.exceptions import ItemCreationError
        try:
            prev = Item()
            next = Item()
            item = Item(next_item=next, prev_item=prev, element="Something")
            print(item)
        except:
            self.fail("Item cannot be created or initialized")
