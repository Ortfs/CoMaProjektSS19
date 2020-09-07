def parse_word(v):
    """fuege die Eingabe als int in eine Liste hinzu"""
    N = [int(x) for x in v.split()]
    if N == []:
        T = [[]]
        return T
    else:
        T = [[N[0]]]

    for i in range(1, len(N)):
        if N[i] < N[i-1]:
            T.append([])
        T[-1].append(N[i])

    """die Anzahl der Kaestchen pro Reihe faellt nicht"""
    for i in range(len(T)-1):
        for j in range(i+1, len(T)):
            if len(T[i]) > len(T[j]):
                raise ValueError("no young tableau")

    """innerhalb jeder Spalte steigen die Zahlen nicht strikt"""
    for i in range(len(T)-1):
        for j in range(i+1, len(T)):
            for k in range(len(T[i])):
                if T[i][k] <= T[j][k]:
                    raise ValueError("no young tableau")


    return T


def parse(row, file):
    with open(file, mode = 'r', encoding='utf-8') as f:
        lines = f.readlines()

    return parse_word(lines[row])


#v = '3 '
#v = '3 4 5 6 2 3'
#v = '5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5'

