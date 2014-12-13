__author__ = 'Udara'
from bst import BinarySearchTree, EmptyValue
##tree i use for testing http://puu.sh/dsvBN/dbe749f41d.png

def num_items(T,item):
    if T.is_empty():
        return 0
    elif T.root != item:
        return num_items(T.left,item)
    else:
        return 1 + num_items(T.left, item)



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

print(num_items(a,3))