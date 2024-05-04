from curses import ncurses_version


nCarros = int(input())

carros = []
for i in range(nCarros):
    q = input()
    q = q.split(" - ")
    met = q[0]
    mat = q[1]
    if met == "aceitarCarro":
        if mat not in carros:
            carros += [mat]
    elif met == "sairCarro":
        for j in range(len(carros)):
            if carros[j] == mat:
                del carros[j]
                break;

print(len(carros))
carros.sort()
for i in range(len(carros)):
    print(carros[i])