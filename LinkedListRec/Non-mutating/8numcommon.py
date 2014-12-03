__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue



def num_common(L1,L2):
    if L1.first is EmptyValue:
        return 0
    elif contains(L2,L1.first):
        return 1 + num_common(L1.rest,L2)
    else:
        return num_common(L1.rest,L2)


def contains(L,item):
    if L.first is EmptyValue:
        return False
    elif L.first == item:
        return True
    else:
        return contains(L.rest,item)

x = LinkedListRec([1,2,3])
y = LinkedListRec([4,5,6,7,3,3])
print(num_common(x,y))