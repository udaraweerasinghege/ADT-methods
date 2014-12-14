__author__ = 'Udara'
def size(T):
    if T.is_empty():
        return 0
    else:
        return 1 + size(T.left)  + size(T.right)


def find_k_large(T,k):
    right = size(T.right)
    if right == k-1:
        return T.root
    elif right < k-1:
        return find_k_large(T.left, k-right-1)
    else:
        return find_k_large(T.right, k)
