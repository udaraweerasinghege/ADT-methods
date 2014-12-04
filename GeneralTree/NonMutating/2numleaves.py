__author__ = 'Udara'
from tree import Tree,EmptyValue

def num_leaves(T):
    if T.root is EmptyValue:
        return 0
    elif T.subtrees == []:
        return 1
    else:
        count = 0
        for subtree in T.subtrees:
            count += num_leaves(subtree)
        return count


a = Tree(1)
b = Tree(2)
c = Tree(3)

d = Tree(4)
e = Tree(5)

b.subtrees = [d,e]
a.subtrees = [b,c]

print(num_leaves(a)) #should be 3