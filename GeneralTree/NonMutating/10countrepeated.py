__author__ = 'Udara'
from tree import Tree,EmptyValue

#again theres  a way to reduce this to a single funciton not sure how.
def count_dups(T):
    return count_dups1(T,[])


def count_dups1(T,seen):
    if T.root is EmptyValue:
        return 0
    elif T.root in seen:
        count = 0
        for tree in T.subtrees:
            count += count_dups1(tree,seen)
        return count
    else:
        seen.append(T.root)
        count = 0
        for tree in T.subtrees:
            count += count_dups1(tree,seen)
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

print(count_dups(a))#1
print(count_dups(b))#0
