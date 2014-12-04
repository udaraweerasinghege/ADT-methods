__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue, convertlst

def remove_dup(L):
    remove_dup_help(L,[])


def remove_dup_help(L,seen):
    if L.first is EmptyValue:
        pass
    elif L.first in seen:
        remove_first(L)
        remove_dup_help(L,seen)
    else:
        seen.append(L.first)
        remove_dup_help(L.rest,seen)


def remove_first(L):
    if L.first is EmptyValue:
        raise IndexError
    else:
        L.first = L.rest.first
        L.rest = L.rest.rest

x = LinkedListRec([1,2,2,3,4,4])
remove_dup(x)
print(convertlst(x))