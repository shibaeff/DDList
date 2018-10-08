class DoublyLinkedListException(Exception):
    def __init__(self):
        pass


class ItemCreationError(DoublyLinkedListException):
    def __init__(self, item):
        self.__context__ = "Error while creation of Item. %v" % item


class EmptyListOperationError(DoublyLinkedListException):
    def __int__(self):
        pass


class PoppedFromEmptyList(EmptyListOperationError):
    def __init__(self):
        pass


class UpshiftingFromEmptyList(EmptyListOperationError):
    def __init__(self):
        pass


