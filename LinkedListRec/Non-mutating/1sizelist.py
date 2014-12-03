from linkedlistrec import LinkedListRec, EmptyValue


def size(L):
    if L.first is EmptyValue:
        return 0
    else:
        return 1 + size(L.rest)

test = LinkedListRec([1,2,3,4,5])
print(size(test) == 5)
