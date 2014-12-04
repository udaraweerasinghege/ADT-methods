__author__ = 'Udara'

from linkedlistrec import LinkedListRec, EmptyValue, convertlst

def insert_back(L,item):
    if L.first is EmptyValue:
        L.first = item
        L.rest = LinkedListRec([])
    else:
        insert_back(L.rest,item)

x = LinkedListRec([1,2,3,4])
insert_back(x,0)

print(convertlst((x)))