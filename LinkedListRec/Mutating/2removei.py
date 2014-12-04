__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue, convertlst

def remove_i(L,i):
    if L.first is EmptyValue:
        raise IndexError
    if i == 0:
        remove_first(L)
    else:
        remove_i(L.rest,i-1)

def remove_first(L):
    if L.first is EmptyValue:
        raise IndexError
    else:
        L.first = L.rest.first
        L.rest = L.rest.rest

x = LinkedListRec([1,2,3])
remove_i(x,2)
print(convertlst(x))