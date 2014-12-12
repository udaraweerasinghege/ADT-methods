__author__ = 'Udara'
from tree import Tree,EmptyValue

def sum_items(T):
    if T.root is EmptyValue:
        return 0
    else:
        count = T.root
        for tree in T.subtrees:
            count += sum_items(tree)
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

print(sum_items(a) == 8+8+7+6+5+4+3+2+1)
print(sum_items(b)) #11