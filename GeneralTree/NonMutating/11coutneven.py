__author__ = 'Udara'
from tree import Tree,EmptyValue

def count_even(T):
    if T.root is EmptyValue:
        return 0
    elif T.root %2 == 0:
        count = 1
        for tree in T.subtrees:
            count += count_even(tree)
        return count
    else:
        count = 0
        for tree in T.subtrees:
            count += count_even(tree)
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

print(count_even(a))#5
print(count_even(b))#2