__author__ = 'Udara'
from tree import Tree,EmptyValue

def count_item(T,item):
    if T.root is EmptyValue:
        return 0
    elif T.root == item:
        return 1
    else:
        count = 0
        for subtree in T.subtrees:
            count += count_item(subtree, item)
        return count


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

print(count_item(a,8))#2
