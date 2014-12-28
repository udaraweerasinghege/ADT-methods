__author__ = 'Pavitheran'

from heap import Heap

def numl(hlst, index):
    if index*2 >= len(hlst):
        return 1
    elif index*2+1 >= len(hlst):
        return numl(hlst, index*2)
    else:
        return numl(hlst, index*2) + numl(hlst, index*2+1)

def numleaves(aheap):
    #Assumes non-empty heap input
    return numl(aheap.items, 1)

