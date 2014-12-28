__author__ = 'Pavitheran'


from heap import Heap

def numi(hlst, index):
    if index*2 >= len(hlst):
        return 0
    elif index*2+1 >= len(hlst):
        return 1
    else:
        return 1 + numi(hlst, index*2) + numi(hlst, index*2+1)

def numinternal(aheap):
    #Assumes non-empty heap input
    return numi(aheap.items, 1)

