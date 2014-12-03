from linkedlistrec import LinkedListRec, EmptyValue

def repeated(L):
    """
    True if some item repeated in L
    """
    return repeated2(L,[])


def repeated2(L,lst):
    if L.first is EmptyValue:
        return False
    if L.first in lst:
        return True
    else:
        lst.append(L.first)
        return repeated2(L.rest,lst)


print(repeated(LinkedListRec([])))#false
print(repeated(LinkedListRec([2]))) #false
print(repeated(LinkedListRec([2,3,4])))#fa;se
print(repeated(LinkedListRec([2,3,3,4])))#true