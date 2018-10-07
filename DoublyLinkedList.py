class Item(object):
    """
    This class is a base class for List's items
    """
    def __init__(self, element=None, next_item=None, prev_item=None):
        self._element = element
        self._next_item = next_item
        self._prev_item = prev_item

    @property
    def element(self):
        return self._element

    @element.setter
    def set_element(self, value):
        self._element = value

    @property
    def next_item(self):
        return self._next_item

    @next_item.setter
    def set_next_item(self, value):
        self._next_item = value

    @property
    def prev_item(self):
        return self._prev_item

    @prev_item.setter
    def set_prev_item(self, value):
        self._prev_item = value

    def __repr__(self):
        return "Item contains " + str(self.element)


class DoublyLinkedList(object):
    def __init__(self, tolearance=None):
        """
        _items is a holder for the Items
        _error_tolerance defines the the DoublyLinkedList behaviour
        when erros occur. None means 0-tolerance, any other value
        means high tolerance.
        """
        self._items = []
        self._error_tolerance = tolearance

    def is_empty(self):
        """
        Checks if list is empy
        :return:
        """
        return len(self._items) == 0

    def push(self, element):
        """
        Pushes element to the tail
        :param element: value to push
        :return:
        """
        if not self.is_empty():
            new_item = Item(prev_item=self._items[-1],
                            next_item=None,
                            element=element)
            self._items.append(new_item)
        else:
            new_item = Item(prev_item=None,
                            next_item=None,
                            element=element)
            self._items.append(new_item)

    def pop(self):
        """
        Pops element from the tail. Returns success in terms of bool.
        List might be empty.
        :return:
        """
        from Exceptions.exceptions import PoppedFromEmptyList
        if self.is_empty() and self._error_tolerance is None:
            raise PoppedFromEmptyList
        elif self.is_empty() and self._error_tolerance is not None:
            return False
        else:
            self._items.pop(-1)
            return True




