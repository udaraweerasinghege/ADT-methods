__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue, convertlst


def remove_first(L):
    if L.first is EmptyValue:
        raise IndexError
    else:
        L.first = L.rest.first
        L.rest = L.rest.rest
x = LinkedListRec([1,2,3])
print(convertlst(x))
