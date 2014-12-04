__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue, convertlst

def remove_after1(L):
    if L.first is EmptyValue:
        raise IndexError
    elif L.first == 1 :
        L.rest = LinkedListRec([])
    else:
        remove_after1(L.rest)

x = LinkedListRec([6,7,8,9,1,2,3,4])

remove_after1(x)
print(convertlst(x))