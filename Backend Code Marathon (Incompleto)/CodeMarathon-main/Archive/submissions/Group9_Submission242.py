casas, noites = input().split(" ")
noites = int(noites)
casas = [int(i) for i in casas]

def noite(casas):
    new = []
    for i in range(6):
        if casas[i-1] - casas[i+1] == 0:
            new.append(1)
        else:
            new.append(0)
    if casas[0] - casas[-2] == 0:
        new.append(1)
    else:
        new.append(0)
    return new

for i in range(noites):
    casas = noite(casas)

casas = [str(i) for i in casas]
print(''.join(casas))