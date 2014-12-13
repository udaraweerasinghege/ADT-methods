__author__ = 'Udara'

from bst import BinarySearchTree, EmptyValue
##tree i use for testing http://puu.sh/dsvBN/dbe749f41d.png
def find_min(T):
    if T.is_empty():
        return 0
    elif T.left.is_empty():
        return T.root
    else:
        return find_min(T.left)





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

print(find_min(c))