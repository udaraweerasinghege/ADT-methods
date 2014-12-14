__author__ = 'Udara'
from bst import BinarySearchTree, EmptyValue
##tree i use for testing http://puu.sh/dsvBN/dbe749f41d.png

#assumes none emtpy
def remove_min(T):
    if T.left.is_empty():
        temp = T.root
        t1L = T.right.left
        t1R = T.right.right
        T.root = T.right.root
        T.left = t1L
        T.right = t1R
        return temp
    else:
        return remove_min(T.left)



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

print(remove_min(a))
print(c.root)
print(c.right.root)
