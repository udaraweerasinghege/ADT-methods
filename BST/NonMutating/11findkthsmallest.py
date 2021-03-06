__author__ = 'Udara'

from bst import BinarySearchTree, EmptyValue
##tree i use for testing http://puu.sh/dsvBN/dbe749f41d.png

#assumes proper k value
def find_kth_smallest(T,k):
    left = size(T.left)
    if left == k-1:
        return T.root
    elif left < k-1:
        return find_kth_smallest(T.right,k-left-1)
    else:
        return find_kth_smallest(T.left,k)

def size(T):
    if T.is_empty():
        return 0
    else:
        return 1 + size(T.left)  + size(T.right)


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

print(find_kth_smallest(a,3))