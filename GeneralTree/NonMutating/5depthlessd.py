__author__ = 'Udara'
from tree import Tree,EmptyValue

def depthlessd(T,d):
    if d==0:
        return 1
    else:
        count = 1  #only difference from pervios exercise
        for trees in T.subtrees:
            count += depthlessd(trees,d-1)
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

print(depthlessd(a,1))#3
print(depthlessd(a,2))#7