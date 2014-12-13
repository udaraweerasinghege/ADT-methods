__author__ = 'Udara'
from tree import Tree,EmptyValue

def remove_root(T):
    if T.subtrees == []:
        T.root = EmptyValue
    else:
        temp = T.subtrees.pop()
        T.root = temp.root
        T.subtrees += temp.subtrees



