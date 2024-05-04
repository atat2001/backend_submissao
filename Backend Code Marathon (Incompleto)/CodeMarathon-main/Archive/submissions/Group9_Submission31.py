
galhos = int(input())

def play(galhos, i):
    if (galhos - 1 == 0 or galhos - 2 == 0 or galhos - 3 == 0) and i % 2 != 0:
        return True
    elif (galhos - 1 == 0 or galhos - 2 == 0 or galhos - 3 == 0) and i % 2 == 0:
        return False
    else:
        i += 1
        return play(galhos - 1, i) or play(galhos - 2, i) or play(galhos - 3, i)


if play(galhos, 0):
    print("vencedor")
else:
    print("perdedor")