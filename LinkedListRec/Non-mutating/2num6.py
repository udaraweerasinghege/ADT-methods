from linkedlistrec import LinkedListRec, EmptyValue

def num6(L):
    if L.first is EmptyValue:
        return 0
    elif L.first == 6:
        return 1 + num6(L.rest)
    else:
        return num6(L.rest)


test = LinkedListRec([1,2,3,4])
print(num6(test)==0)
test1 = LinkedListRec([1,2,3,4,6,6])
print(num6(test1)==2)
test1 = LinkedListRec([6,2,6,3,4,6])
print(num6(test1)==3)