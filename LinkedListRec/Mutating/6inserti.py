__author__ = 'Udara'
__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue, convertlst

def insert(L,i,item):
    if i == 0:
        insert_front(L,item)
    else:
        insert(L.rest,i-1,item)

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
insert(x,1,0)
print(convertlst((x)))