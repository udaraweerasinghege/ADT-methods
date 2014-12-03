from linkedlistrec import LinkedListRec, EmptyValue

def sum(L):
    if L.first is EmptyValue:
        return 0
    else:
        return L.first + sum(L.rest)

test = LinkedListRec([0])
print(sum(test) == 0)

test1 = LinkedListRec([0,1,2,3,4])
print(sum(test1) == 10)