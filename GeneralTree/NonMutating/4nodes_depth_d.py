__author__ = 'Udara'
from tree import Tree,EmptyValue
#This is a cheap way to do this, im sure there is an easier way

#this function finds nodes at depth < d

def depth(T,d):
    """
    assumes proper D that isn't too big or anything

    """
    if d == 0:
        return 1
    else:
        count= 0
        for trees in T.subtrees:
            count += depth(T,d-1)
        return count





a = Tree(1)
b = Tree(2)
c = Tree(3)

d = Tree(4)
e = Tree(5)

f = Tree(6)
g = Tree(7)

c.subtrees = [f,g]
b.subtrees = [d,e]
a.subtrees = [b,c]

print(depth(a,1))#2
print(depth(a,2))#4