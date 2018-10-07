class DoublyLinkedListException(Exception):
    def __init__(self):
        pass


class ItemCreationError(DoublyLinkedListException):
    def __init__(self, item):
        self.__context__ = "Error while creation of Item. %v" % item


class PoppedFromEmptyList(Exception):
    def __init__(self):
        pass

