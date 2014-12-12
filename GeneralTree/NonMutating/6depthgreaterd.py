__author__ = 'Udara'
from tree import Tree,EmptyValue
#This is a cheap way to do this, im sure there is an easier way


def depth_greater(T,d):
    return size(T) - depthlessd(T , d-1)

def depthlessd(T,d):
    if d== 0:
        return 1
    else:
        count = 1  #only difference from pervios exercise
        for trees in T.subtrees:
            count += depthlessd(trees,d-1)
        return count

def size(T):
    if T.root is EmptyValue:
        return 0
    else:
        count = 1
        for tree in T.subtrees:
            count += size(tree)
        return count






a = Tree(1)
b = Tree(2)
c = Tree(3)

d = Tree(4)
e = Tree(5)

f = Tree(6)
g = Tree(7)

h = Tree(8)

g.subtrees= [h]
c.subtrees = [f,g]
b.subtrees = [d,e]
a.subtrees = [b,c]

print(depth_greater(a,2))