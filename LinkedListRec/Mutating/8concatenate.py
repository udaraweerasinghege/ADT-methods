__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue, convertlst

def concat(L1,L2):
    if L1.first is EmptyValue:
        L1.first = L2.first
        L1.rest = L2.rest
    else:
        concat(L1.rest,L2)

x = LinkedListRec([1])
y = LinkedListRec([3,4,5,6])
concat(x,y)
print(convertlst(x))