__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue, convertlst

def remove_firstn(L,n):
    if n==0:
        pass
    else:
        remove_first(L)
        remove_firstn(L,n-1)



def remove_first(L):
    if L.first is EmptyValue:
        raise IndexError
    else:
        L.first = L.rest.first
        L.rest = L.rest.rest

x = LinkedListRec([1,2,3])
remove_firstn(x,3)
print(convertlst(x))