__author__ = 'Udara'
from linkedlistrec import LinkedListRec, EmptyValue
def listdup(L):
    return listdup2(L,[],[])


def listdup2(L,seen,dups):
    if L.first is EmptyValue:
        return dups
    elif L.first in seen and L.first not in dups:
        dups.append(L.first)
        return listdup2(L.rest,seen,dups)
    else:
        seen.append(L.first)
        return listdup2(L.rest,seen,dups)

x  = LinkedListRec([1,2,3,4,4,4,4,4])
print(listdup(x))