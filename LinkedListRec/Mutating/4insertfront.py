__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue, convertlst

def insert_front(L,item):
    if L.first is EmptyValue:
        L.first = item
        L.rest = LinkedListRec([])
    else:
        temp = LinkedListRec([])
        temp.first = L.first
        temp.rest = L.rest
        L.first = item
        L.rest = temp

x = LinkedListRec([1,2,3])
insert_front(x,0)
print(convertlst((x)))
