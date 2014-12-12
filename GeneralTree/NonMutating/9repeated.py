__author__ = 'Udara'
from tree import Tree,EmptyValue

#theres definitely a way to do this with one function but it didnt come to me :(

def repeated(T):
    return repeated_1(T,[])


def repeated_1(T, seen):
    #redundant, but how to handle this?
    if T.root is EmptyValue:
        pass
    elif T.root in seen:
        return True
    else:
        seen.append(T.root)
        for tree in T.subtrees:
            if repeated_1(tree,seen):
                return True
        return False


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

print(repeated(a))#True
print(repeated(b))#False
