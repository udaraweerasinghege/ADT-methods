__author__ = 'Udara'
__author__ = 'Udara'
from bst import BinarySearchTree, EmptyValue
##tree i use for testing http://puu.sh/dsvBN/dbe749f41d.png
def depth(T,d):
    if T.is_empty():
        return 0
    elif d == 0:
        return 1
    else:
        return depth(T.right,d-1) + depth(T.right,d-1)





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

print(depth(a,2))