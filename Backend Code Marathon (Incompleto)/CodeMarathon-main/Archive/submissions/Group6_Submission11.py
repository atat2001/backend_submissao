from random import randint 
galhos = int(input("Numero de galhos: "))
toze = 0
eu = 0
i = 0
while galhos > 3:
    galhos -= randint(1,3)
    if i % 2 == 0: toze += 1
    else: eu += 1
    i += 1

if toze > eu:
    print("vencedor")
else:
    print("perdedor")
