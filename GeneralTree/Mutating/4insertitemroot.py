__author__ = 'Udara'
from tree import Tree,EmptyValue

def insert_root(T ,item):
    if T.is_empty():
        T.root = item
        T.subtrees = []
    else:
        temp1 = T.root
        T.root = item
        T.subtrees.append(Tree(temp1))

a = Tree(1)
b = Tree(2)
c = Tree(3)

d = Tree(4)
e = Tree(5)

f = Tree(6)
g = Tree(7)

h = Tree(8)

i = Tree(8)

g.subtrees= [h,i]
c.subtrees = [f,g]
b.subtrees = [d,e]
a.subtrees = [b,c]

insert_root(a,111)
print(a.root)
print(a.subtrees[0].root)
print(a.subtrees[-1].root)