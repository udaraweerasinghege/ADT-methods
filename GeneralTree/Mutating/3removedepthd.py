__author__ = 'Udara'
from tree import Tree,EmptyValue
#does this even work?

def remove_d(T,d):
    if d == 0:
        remove_root(T)
    else:
        for tree in T.subtrees:
            remove_d(tree,d-1)





def remove_root(T):
    if T.subtrees == []:
        T.root = EmptyValue
    else:
        temp = T.subtrees.pop()
        T.root = temp.root
        T.subtrees += temp.subtrees