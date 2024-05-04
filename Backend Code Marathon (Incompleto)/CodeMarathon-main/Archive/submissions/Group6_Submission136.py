numero = int(input())
lista = []
for i in range(1, numero + 1):
    lista.extend([int(a) for a in str(i)])
value = lista.count(1) + lista.count(0)
print(value)

