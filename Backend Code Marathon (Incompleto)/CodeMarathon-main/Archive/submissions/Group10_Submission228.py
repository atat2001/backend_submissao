import string


def Par_aux(x, y):
    if x == y:
        return(True)
    else:
        return(False)

def Par(n):

    cont = 0

    string = str(n)

    if len(n) == 1:
        return 0

    for i in range(len(string)):
        for h in range(len(string)):
            if Par_aux(string[i], string[h]) and i < h:
                cont += 1

    return cont
