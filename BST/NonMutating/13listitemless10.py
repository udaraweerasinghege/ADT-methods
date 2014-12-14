__author__ = 'Udara'

from bst import BinarySearchTree, EmptyValue
##tree i use for testing http://puu.sh/dsvBN/dbe749f41d.png

#assumes proper k value
def less_10(T):
    if T.is_empty():
        return []
    else:
        x=[]
        if T.root <=10:
            x.append(T.root)
        x.extend(less_10(T.left))
        x.extend(less_10(T.right))
        return x

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

print(less_10(a))