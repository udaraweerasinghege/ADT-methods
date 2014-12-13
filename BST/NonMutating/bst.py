__author__ = 'Udara'
class EmptyValue:
    pass

class BinarySearchTree:
    def __init__(self, root=EmptyValue):
        self.root = root    # root value
        if self.is_empty():
            # Set left and right to nothing,
            # because this is an empty binary tree.
            self.left = None
            self.right = None
        else:
            # Set left and right to be new empty trees.
            # Note that this is different than setting them to None!
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()

    def is_empty(self):
        return self.root is EmptyValue