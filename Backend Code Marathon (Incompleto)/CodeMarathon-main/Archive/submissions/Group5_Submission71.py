inp = int(input())

cont = 0
for nr in range(1, inp + 1):
    nrEmStr = str(nr)
    for c in nrEmStr:
        if c == "0" or c == "1":
            cont += 1

print(cont)
