from unittest import TestCase


class TestDoublyLinkedList(TestCase):
    def test_push(self):
        from DoublyLinkedList import DoublyLinkedList
        list = DoublyLinkedList()

        # push to the empty list
        list.push("1st")
        print(list._items)

        self.assertEqual("1st", list._items[-1].element)

        # push once again
        list.push("2nd")

        self.assertEqual("2nd", list._items[-1].element)

        # little big stress test
        for i in range(1000):
            list.push(i)
            self.assertEqual(i, list._items[-1].element)