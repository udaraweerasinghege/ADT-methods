__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue

def merge(L1,L2):
    if L1.first is EmptyValue and L2.first is EmptyValue:
        return LinkedListRec([])
    elif L1.first is EmptyValue:
        return L2
    elif L2.first is EmptyValue:
        return L1
    elif L1.first <= L2.first:
        new_lst = LinkedListRec([L1.first])
        new_lst.rest = merge(L1.rest,L2)
        return new_lst
    else:
        new_lst = LinkedListRec([L2.first])
        new_lst.rest = merge(L1,L2.rest)
        return new_lst

#this is here just to see results
def convertlst(L):
    if L.first is EmptyValue:
        return []
    else:
        return [L.first] + convertlst(L.rest)

x = LinkedListRec([1,3,6])
#print(convertlst(x))
y = LinkedListRec([4,5,7])
#print(convertlst(y))
z = merge(x,y)
print(convertlst(z))