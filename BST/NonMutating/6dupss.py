__author__ = 'Udara'
from bst import BinarySearchTree, EmptyValue
##tree i use for testing http://puu.sh/dsvBN/dbe749f41d.png
def dups(T):
    return dupsx(T,[])

def dupsx(T,seen):
    if T.is_empty():
        return 0
    elif T.root in seen:
        return 1 + dupsx(T.left, seen) + dupsx(T.right, seen)
    else:
        seen.append(T.root)
        return dupsx(T.left, seen) + dupsx(T.right, seen)





a = BinarySearchTree(10)
b = BinarySearchTree(5)
c = BinarySearchTree(20)

d = BinarySearchTree(3)
e = BinarySearchTree(7)

f = BinarySearchTree(18)
g = BinarySearchTree(22)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

d.left = BinarySearchTree(3)
f.left = BinarySearchTree(18)
e.left = BinarySearchTree(7)
g.left = BinarySearchTree(22)

print(dups(a))