__author__ = 'Udara'
from tree import Tree,EmptyValue
import random
#this is Simeon Krastnikov's solution from https://piazza.com/class/hyqnburtpcn441?cid=822

def restructure_d(T,d):
    if T.is_empty():
        pass
    else:
        x = 0
        while len(T.subtrees) > d:
            T.subtrees[x].add_subtrees([T.subtrees.pop()])
            x = (x+1)%d

        for tree in T.subtrees:
            restructure_d(tree,d)

