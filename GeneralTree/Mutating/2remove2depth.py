__author__ = 'Udara'
from tree import Tree,EmptyValue
#probably not how we're meant to do this...
def remove_at_depth2(T):
    for tree in T.subtrees:
        for tree1 in tree:
            remove_root(tree1)


def remove_root(T):
    if T.subtrees == []:
        T.root = EmptyValue
    else:
        temp = T.subtrees.pop()
        T.root = temp.root
        T.subtrees += temp.subtrees