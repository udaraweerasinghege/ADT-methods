__author__ = 'Udara'
from bst import BinarySearchTree, EmptyValue
##tree i use for testing http://puu.sh/dsvBN/dbe749f41d.png

def internal(T):
    if T.is_empty():
        return 0
    elif T.left.is_empty() and T.right.is_empty():
        return 0
    else:
        return 1 + internal(T.left) +  internal(T.right)







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

print(internal(a))