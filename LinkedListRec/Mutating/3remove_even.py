__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue, convertlst

def remove_even(L):
    if L.first is EmptyValue:
        pass
    elif L.first %2 == 0:
        remove_first(L)
        #once removed, list could be empty now
        if L.first is not EmptyValue:
            remove_even(L)
    else:
        remove_even(L.rest)

def remove_first(L):
    if L.first is EmptyValue:
        raise IndexError
    else:
        L.first = L.rest.first
        L.rest = L.rest.rest

x = LinkedListRec([2,4,7,8])
remove_even(x)
print(convertlst(x))
