__author__ = 'Udara'
class EmptyValue:
    """As with linked lists, we'll use this class
    as a dummy class to signify the root of an empty tree.
    """
    pass


class Tree:
    """A recursive tree data structure.

    Attributes:
    - root (object): the item stored at the root of the tree,
                     or EmptyValue if the tree is empty.
    - subtrees (list of Tree): a list of all subtrees of the tree
    """

    def __init__(self, root=EmptyValue):
        """ (Tree, object) -> NoneType

        Create a new tree with given root value.
        If no root value is passed in, the tree is empty
        (this is signified by setting the root value to EmptyValue).
        A new tree always has no subtrees.
        """
        self.root = root
        self.subtrees = []

    def print_tree(self):
        """ (Tree) -> NoneType

        Print all of the items in this tree,
        where the root is printed before all of its subtrees.
        """
        if not self.is_empty():
            # This prints the root item before all of the subtrees.
            print(self.root)
            for subtree in self.subtrees:
                subtree.print_tree()

        # Or alternately, simply call
        # self.print_tree_indent()

    def print_tree_indent(self, depth=0):
        """ (Tree) -> NoneType

        Print all of the items in this tree,
        where the root is printed before all of its subtrees,
        and every value is indented to show its depth.
        """
        if not self.is_empty():
            print(depth * '  ' + str(self.root))
            for subtree in self.subtrees:
                subtree.print_tree_indent(depth + 1)