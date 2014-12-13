__author__ = 'Udara'
from tree import Tree,EmptyValue

def insertD(T,d,item):
    #assumes proper d
    if d-1 == 0:
        T.subtrees.append(Tree(item))
    elif d == 0:
        insert_root(T,d)
    else:
        insertD(T.subtrees[0],d-1,item)






def insert_root(T ,item):
    if T.is_empty():
        T.root = item
        T.subtrees = []
    else:
        temp1 = T.root
        T.root = item
        T.subtrees.append(Tree(temp1))
