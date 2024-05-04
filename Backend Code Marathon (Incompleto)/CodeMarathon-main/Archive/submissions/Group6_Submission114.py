input, valor = input().split(",")
print(input, valor)
value = tuple(input)
descod = ''
for letra in value:
    try:
        repeat = int(letra)
        for i in range(1, repeat):
            descod += descod
    except:
        descod += letra
print(descod[int(valor) - 1])
