from unittest import TestCase
from DoublyLinkedList import DoublyLinkedList


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

    def test_pop(self):
        list = DoublyLinkedList()

        # pop from the empty list, error should be raised
        from Exceptions.exceptions import PoppedFromEmptyList
        with self.assertRaises(PoppedFromEmptyList):
            list.pop()

        # changing error tolerance
        list._error_tolerance = "ok"
        # just bool is returnd
        self.assertEqual(False, list.pop())

    def test_push_pop(self):
        # some push-pop random routine
        list = DoublyLinkedList(tolearance="LGBTq")
        from random import randint
        for i in range(20):
            list.push(i)
            self.assertEqual(i, list._items[-1].element)

        while not list.is_empty():
            if randint(0, 1):
                new_int = randint(0, 1000)
                list.push(new_int)
                self.assertEqual(new_int, list._items[-1].element)
            else:
                prev = list._items[-2]
                list.pop()
                self.assertEqual(prev, list._items[-1])

    def test_shift(self):
        list = DoublyLinkedList()
        # little big stress test
        for i in range(1000):
            list.shift(i)
            self.assertEqual(i, list._items[0].element)

    def test_shift_upshift(self):
        # some push-pop random routine
        list = DoublyLinkedList(tolearance="LGBTq")
        from random import randint
        for i in range(20):
            list.shift(i)
            self.assertEqual(i, list._items[0].element)

        while not list.is_empty():
            if randint(0, 1):
                new_int = randint(0, 1000)
                list.shift(new_int)
                self.assertEqual(new_int, list._items[0].element)
            else:
                next = list._items[1]
                list.upshift()
                self.assertEqual(next, list._items[0])

    def test_contains(self):
        list = DoublyLinkedList(tolearance="straight")
        for i in range(20):
            list.shift(i)
            self.assertEqual(i, list._items[0].element)
        for i in range(20):
            self.assertEqual(True, list.contains(i))
