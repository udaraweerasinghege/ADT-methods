__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue, convertlst

def remove_lastn(L,n):
    if n ==0:
        pass
    else:
        remove_last(L)
        remove_lastn(L,n-1)

def remove_last(L):
    if L.first is EmptyValue:
        raise IndexError
    elif L.rest.first is EmptyValue:
        L.first = EmptyValue
        L.rest= None
    else:
        remove_last(L.rest)

x = LinkedListRec([1,2,3,4,5,6,7,8,9,10])
remove_lastn(x,5)
print(convertlst(x))