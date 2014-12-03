from linkedlistrec import LinkedListRec, EmptyValue

def numitem(L,item):
    if L.first is EmptyValue:
        return 0
    elif L.first == item:
        return 1 + numitem(L.rest,item)
    else:
        return numitem(L.rest,item)


test = LinkedListRec([1,2,3,4])
print(numitem(test,6)==0)
test1 = LinkedListRec([1,2,3,4,6,6])
print(numitem(test1,2)==1)
test1 = LinkedListRec([6,2,6,3,4,6])
print(numitem(test1,4)==1)
