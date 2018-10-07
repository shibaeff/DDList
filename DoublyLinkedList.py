class Item:
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
        return "Item contains %v" % self.element



