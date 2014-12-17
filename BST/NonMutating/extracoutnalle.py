__author__ = 'Udara'

from bst import BinarySearchTree, EmptyValue
##tree i use for testing http://puu.sh/dsvBN/dbe749f41d.png
def count_all(T,item):
    if T.is_empty():
        return 0
    elif T.root < item:
        return count_all(T.right, item)
    elif T.root > item:
        return count_all(T.left,item)
    else:
        #return 1 + count_all(T.left, item)
        n = 1
        n+= count_all(T.left,item)
        return n






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

g.left = BinarySearchTree(22)
print(count_all(a,22))