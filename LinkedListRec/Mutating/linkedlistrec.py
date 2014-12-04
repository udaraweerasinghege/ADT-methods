class EmptyValue:
    pass

class LinkedListRec:
    """Linked List with a recursive implementation.
    Note that there is no "Node" class with this implementation.

    Attributes:
    - first (object): the first item stored in this list,
                      or EmptyValue if this list is empty
    - rest (LinkedListRec): a list containing the other items
                            in this list, or None if this list is empty
    """

    def __init__(self, items):
        """ (LinkedListRec, list) -> NoneType

        Create a new linked list containing the elements in items.
        If items is empty, self.first initialized to EmptyValue.
        """
        if len(items) == 0:
            self.first = EmptyValue
            self.rest = None
        else:
            self.first = items[0]
            self.rest = LinkedListRec(items[1:])

def convertlst(L):
    if L.first is EmptyValue:
        return []
    else:
        return [L.first] + convertlst(L.rest)