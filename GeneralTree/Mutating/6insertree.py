__author__ = 'Udara'
from tree import Tree,EmptyValue
#inserts at the end of a tree (a tree with no subtrees
def insert_tree(T,tree):
    if T.is_empty():
        T.root = tree.root
        T.subtrees = tree.subtrees
    elif T.subtrees == []:
        T.subtrees.append(tree)
    else:
        insert_tree(T.subtrees[0],tree)