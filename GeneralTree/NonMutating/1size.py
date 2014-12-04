__author__ = 'Udara'
from tree import Tree,EmptyValue

def size(T):
    if T.root is EmptyValue:
        return 0
    else:
        count = 1
        for subtree in T.subtrees:
            count += size(subtree)
        return count
a = Tree(1)
b = Tree(2)
c = Tree(3)

d = Tree(4)
e = Tree(5)

b.subtrees = [d,e]
a.subtrees = [b,c]

print(size(a)) #should be 5