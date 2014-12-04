__author__ = 'Udara'
from tree import Tree,EmptyValue

def internal_nodes(T):
    if T.root is EmptyValue:
        return 0
    #can't use T.subtrees is [] here.
    #can't use T.subtrees is [] here.
    elif T.subtrees == []:
        return 0
    else:
        count = 1
        for trees in T.subtrees:
            count += internal_nodes(trees)
        return count




a = Tree(1)
b = Tree(2)
c = Tree(3)

d = Tree(4)
e = Tree(5)

b.subtrees = [d,e]
a.subtrees = [b,c]

print(internal_nodes(a))