__author__ = 'Udara'
from tree import Tree,EmptyValue
import random
#this is Simeon Krastnikov's solution from https://piazza.com/class/hyqnburtpcn441?cid=822

def restructure_binary(T):
    if T.is_empty():
        return
    #used to alternate between 0th and 1st subtree to add to
    x = 0
    while len(T.subtrees) > 2:
        T.subtrees[x].add_subtrees([T.subtrees.pop()])
        x = (x + 1) % 2
    for subtree in T.subtrees:
        restructure_binary(subtree)



