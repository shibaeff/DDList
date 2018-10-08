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
    def element(self, value):
        self._element = value

    @property
    def next_item(self):
        return self._next_item

    @next_item.setter
    def next_item(self, value):
        self._next_item = value

    @property
    def prev_item(self):
        return self._prev_item

    @prev_item.setter
    def prev_item(self, value):
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
        self._head = Item()
        self._tail = Item(prev_item=self._head)
        self._head.next_item = self._tail
        self._error_tolerance = tolearance

    def len(self):
        length = 0
        cur_item = self._head
        while cur_item.next_item is not self._tail:
            length += 1
            cur_item = cur_item.next_item
        return length

    def is_empty(self):
        """
        Checks if list is empy
        :return:
        """
        return self.len() == 0

    def first(self):
        """
        Returns the first element
        :return:
        """
        from Exceptions.exceptions import EmptyListOperationError
        if self.is_empty():
            raise EmptyListOperationError
        return self._head.next_item

    def last(self):
        """
        Returns the last element
        :return:
        """
        from Exceptions.exceptions import EmptyListOperationError
        if self.is_empty():
            raise EmptyListOperationError
        return self._tail.prev_item

    def push(self, element):
        """
        Pushes element to the tail
        :param element: value to push
        :return:
        """


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
            self._items[-1].next_item = None
            return True

    def shift(self, element):
        """Adds element to the beginning of the list"""
        if not self.is_empty():
            old = self._items
            new_item = Item(prev_item=None,
                            next_item=old[0],
                            element=element)
            old[0]._prev_item = new_item
            self._items = [new_item] + old
        else:
            new_item = Item(prev_item=None,
                            next_item=None,
                            element=element)
            self._items.append(new_item)

    def upshift(self):
        """
        Deletes from the beginning.
        Raises error according to tolerance level.
        :return: if upshift was succesful
        """
        if self.is_empty():
            if self._error_tolerance is None:
                raise UpshiftingFromEmptyList
            else:
                return False
        else:
            new = self._items[1:]
            new[0]._prev_item = None
            self._items = new
            return True

    def contains(self, element):
        """
        Determines whether value is in the list
        :param element: value to check
        :return: success
        """
        cur_item = self.first()
        while cur_item != self.last():
            if cur_item.element == element:
                return True
            else:
                cur_item = cur_item.next_item
        return cur_item.element == element

    def delete(self, element):
        """
        Deletes item by value
        :param element:
        :return: deletion success
        """
        cur_item = self.first()
        while cur_item != self.last():
            if cur_item.element == element:
                cur_item.prev_item.next_item = cur_item.next_item
                cur_item.next_item.prev_item = cur_item.prev_item
                self._items.remove(cur_item)
                return True
            else:
                cur_item = cur_item.next_item
        return cur_item.element == element

