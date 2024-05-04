datas = input().split(",")
lista = [int(a[4:]) for a in datas]
lista.sort()
idade = [lista[2] - lista[0], (lista[2] - lista[1]) * 7]
print(idade[0] > idade[1])