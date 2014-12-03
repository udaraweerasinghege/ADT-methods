__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue

def count_even(L):
    if L.first is EmptyValue:
        return 0
    elif L.first %2 == 0:
        return 1 + count_even(L.rest)
    else:
        return count_even(L.rest)

print(count_even(LinkedListRec([1,2,3,4])))
print(count_even((LinkedListRec([1,2,3])))) #1