def row_insert(l,x,j):
    '''
    :param l: list
    :param x: integer
    :param: j integer (initially set to 0 to enable recursion)
    :return: l with the new element x inserted in the correct position (determined recursively with the algorithm described in Part 3)
    '''
    l.append([])
    if all(a <= x for a in l[j]) or l[j] == []:
        l[j].append(x)
    else:
       y = findfirst(l[j],x)[1]
       y_index = findfirst(l[j],x)[0]
       l[j][y_index] = x
       row_insert(l,y,j+1)
    if l[-1] == []:
        l.pop()

    return l

def findfirst(l,x):
    return next(y for y in enumerate(l) if y[1] > x)


def listtostring(l):
    '''
    :param l: list
    :return: string (concatenation of elements in l)
    '''
    if l == []:
        return ""
    if len(l) == 1:
        return str(l[0])
    else:
        a = str(l[0])
        for i in range(1,len(l)):
            a += " "
            a += str(l[i])
    return a


def multiply_tab(S, T):
    '''
    :param S: element of class youngtableau
    :param T: element of class youngtableau
    :return: S*T as defined
    '''
    if not S.w.list:
        return T
    elif not T.w.list:
        return S
    else:
        for x in T.w.list:
            S.row_insert(x)
        return S


def K1(l, i):
    if i > len(l) - 3:
        raise ValueError("K-operation impossible")
    y, z, x = l[i], l[i+1], l[i+2]
    if x < y <= z:
        l[i], l[i + 1], l[i + 2] = y, x, z
        return l
    else:
        raise ValueError("K-operation impossible")


def K1_inv(l, i):
    if i > len(l) - 3:
        raise ValueError("K-operation impossible")
    y, x, z = l[i], l[i + 1], l[i + 2]
    if x < y <= z:
        l[i], l[i + 1], l[i + 2] = y, z, x
        return l
    else:
        raise ValueError("K-operation impossible")


def K2(l, i):
    if i > len(l) - 3:
        raise ValueError("K-operation impossible")
    x, z, y = l[i], l[i + 1], l[i + 2]
    if x <= y < z:
        l[i], l[i + 1], l[i + 2] = z, x, y
        return l
    else:
        raise ValueError("K-operation impossible")


def K2_inv(l, i):
    if i > len(l) - 3:
        raise ValueError("K-operation impossible")
    z, x, y = l[i], l[i + 1], l[i + 2]
    if x <= y < z:
        l[i], l[i + 1], l[i + 2] = x, z, y
        return l
    else:
        raise ValueError("K-operation impossible")
