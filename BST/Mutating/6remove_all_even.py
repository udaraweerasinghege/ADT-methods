__author__ = 'Udara'
from bst import BinarySearchTree, EmptyValue

def extract_max(T):
    if T.right.is_empty():
        t1 = T.root
        T.root = T.left.root
        T.right = T.left.right
        newL = T.left.left
        T.left = newL
        return t1
    else:
        return extract_max(T.right)

def delete_root(T):
    #assumees not empty
    #replaces root with largest item form left subtree
    #also possible to do this by setting it to smallest item from right subtree
    T.root = extract_max(T.left)

def alleven(T):
    if T.is_empty():
        return
    elif T.root &2 ==0:
        delete_root(T)
        alleven(T)
    else:
        alleven(T.left)
        alleven(T.right)