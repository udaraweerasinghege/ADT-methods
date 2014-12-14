__author__ = 'Udara'

#even if the number 10 occurs more than once, it's only recorded once in this funciton
#done to improve run time, might not be exactly what's asked of it.

def greater_10(T):
    if T.is_empty():
        return []
    else:
        x=[]
        if T.root >=10:
            x.append(T.root)
        x.extend(greater_10(T.left))
        x.extend(greater_10(T.right))
        return x